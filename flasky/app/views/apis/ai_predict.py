from flask_restful import Resource, reqparse, current_app
from flask import request
# models
from app.models.users import Users
from app.models.stock_basic_info import StockBasicInfo
from app.models.trade_records import TradeRecords
from app.models.stock_data import StockData
# sqlalchemy 條件、公式
from sqlalchemy.sql import func
from sqlalchemy import and_, or_, not_
import pandas
# 引入three_days_price_predict
from app.views.ai.three_days_price_predict import three_days_predict


class AIPredict(Resource):
    def get(self):
        # stock = StockBasicInfo.query.filter_by(stock_symbol='0050').first()
        # stock_data = StockData.query.filter_by(stock_basic_info_id=stock.id).order_by(StockData.date)
        # # 讀取db -> dataframe
        # dataframe = pandas.read_sql(stock_data.statement, StockData.db_session_bind())
        three_days_predict_output = three_days_predict()
        return '123'
        return str(three_days_predict_output)



    def post(self):

        return "123"


