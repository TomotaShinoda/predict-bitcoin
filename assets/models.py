# coding: utf-8
from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, Date
from assets.database import Base
from datetime import datetime as dt

# 作成したいDBの構造を以下に明記

#Table情報
class Data(Base):
    #TableNameの設定
    __tablename__ = "data"
    #Column情報を設定する
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, unique=False)
    real_price = Column(Float, unique=False)
    pred_price = Column(Float, unique=False)
    timestamp = Column(DateTime, default=dt.now())

    def __init__(self, date=None, real_price=None, pred_price=None, timestamp=None):
        self.date = date
        self.real_price = real_price
        self.pred_price = pred_price
        self.timestamp = timestamp