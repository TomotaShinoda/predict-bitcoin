from assets.database import db_session
from assets.models import Data

from keras.models import Sequential
import numpy as np
import requests
import pickle
from datetime import timedelta

# coincheckのAPIから相場情報を取得する関数を作成
def get_price():
    URL = 'https://coincheck.com/api/ticker'
    coincheck = requests.get(URL).json() 
    last_price = coincheck['last']
    
    return last_price

# 翌日の相場を予測し、DBにデータを格納する関数を作成
def predict_nextday():

    # 価格情報を取得しデータフレームに格納
    today_data = db_session.query(Data).all()[-1]
    today_data.real_price = get_price()  # 上書き（上書きする前はNoneになっている）
    db_session.add(today_data)
    db_session.commit()

    # windowを作成し標準化
    window = 5
    data_five = db_session.query(Data).all()[-window:]
    input_will = []

    for price in data_five:
        input_will.append(price.real_price)

    input_will = np.array(input_will).reshape(1, window, 1)
    input_mean = np.mean(input_will)
    input_std = np.std(input_will)
    sta_input = (input_will - input_mean) / input_std

    # 学習済みモデルを取得
    with open("lstm_model.pickle", "rb") as f:
        model = pickle.load(f)

    # 翌日の価格を予測、標準化してあるので元に戻す
    future_price = model.predict(sta_input)
    future_price = future_price.reshape(-1)
    future_price = future_price*input_std + input_mean
    future_price = float(future_price)

    # 翌日の日付を取得
    today = db_session.query(Data).all()[-1].date
    next_day = today + timedelta(days=1)

    # 翌日の日付、予測した価格をデータベースに格納
    row = Data(date = next_day, real_price = None, pred_price = future_price)
    db_session.add(row)
    db_session.commit()

# アプリケーションを起動
if __name__ == "__main__":
    predict_nextday()