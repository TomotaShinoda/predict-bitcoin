# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
import os
import requests
import json
import pandas as pd
import numpy as np
import pickle
from keras.models import Sequential

# DBの初期化に必要な情報を以下に明記

# DBのファイル名、保存場所を記述
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')
# 用いるDBを記述
engine = create_engine(os.environ.get('DATABASE_URL') or 'sqlite:///' + databese_file, convert_unicode=True , echo=True)
# sqlalchemyの設定を記述
db_session = scoped_session(
                sessionmaker(
                    autocommit = False,
                    autoflush = False,
                    bind = engine
                )
             )
Base = declarative_base()
Base.query = db_session.query_property()

# DBの初期化の関数を作成
def init_db():
    #import assets.models
    from assets import models
    Base.metadata.create_all(bind=engine)

# 過去情報をDBに格納する関数を作成
def read_data():
    from assets import models

    # 2019/02/01～の情報を取得（UTCとの時差は9時間）（close_timeは日本時間で午前9時）
    res = requests.get('https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods=86400&after=1548979200')
    data = json.loads(res.text)

    # 取得した情報をデータフレームに格納
    daily_data = pd.DataFrame(data['result']['86400'], columns=['close_time', 'open_price', 'high_price', 'low_price', 'close_price', 'volume', 'quote_volume'])
    daily_data['date'] = pd.to_datetime(daily_data['close_time'], unit='s')
    daily_data = daily_data[:-1] # 最終行を削除（取得した時点の情報が次の日の情報となっているため）

    # 日本時間に変更
    diff_JST_from_UTC = 9
    daily_data['date'] = daily_data['date'] + datetime.timedelta(hours=diff_JST_from_UTC)

    # 過去相場の予測結果をDBに格納するために以下で学習済みモデルへの入力データを作成
    period = 5
    data = daily_data['close_price']

    # 各データをリストに格納するためにリストを作成
    input_tensor = []
    label_tensor = []
    mean_list = []
    std_list = []
    data_len = len(data)    #総データ数

    #変数とラベルの生成
    for i in range(0, data_len - period, 1):
        window = data.values[i:i + period]
        mean = np.mean(window)
        std = np.std(window)
        mean_list.append(mean)
        std_list.append(std)
        input_tensor.append((window-mean) / std)
        label_tensor.append((data.values[i + period]-mean) / std)

    input_tensor = np.array(input_tensor).reshape(len(data)-period, period, 1)
    label_tensor = np.array(label_tensor).reshape(len(data)-period, 1)
    mean_list = np.array(mean_list)
    std_list = np.array(std_list)

    # label_tensorの最初はdaily_data['date']の５列目からなので日付データを整形
    date = daily_data['date'][5:].reset_index(drop=True)

    # 学習済みモデルを取得
    with open("lstm_model.pickle", "rb") as f:
        model = pickle.load(f)

    # 学習済みモデルで予測
    pred = model.predict(input_tensor)
    pred = pred.reshape(-1)
    pred = pred*std_list + mean_list
    label_tensor = label_tensor.reshape(-1)
    real = label_tensor*std_list + mean_list
    past_df = pd.DataFrame({'date':date, 'pred':pred, 'real':real})

    # 過去情報をDBに格納
    for index, _past_df in past_df.iterrows():
        row = models.Data(date = _past_df['date'], real_price = _past_df['real'], pred_price = _past_df['pred'])
        db_session.add(row)

    db_session.commit()