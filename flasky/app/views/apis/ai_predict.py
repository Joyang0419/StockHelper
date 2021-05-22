from flask_restful import Resource, reqparse, current_app
from flask import request
# models
from app.models.users import Users
from app.models.stock_basic_info import StockBasicInfo
from app.models.trade_records import TradeRecords
from app.models.stock_data import StockData
from app.models.three_days_predict import ThreeDaysPredict
# sqlalchemy 條件、公式
from sqlalchemy.sql import func
from sqlalchemy import and_, or_, not_
import pandas
from datetime import timedelta


class AIPredict(Resource):
    def get(self):
        response = {
            'latest_date': None,
            'stock_name': None,
            'three_days_predict': None,
            'five_days_predict': None
        }

        stock = StockBasicInfo.query.filter_by(stock_symbol='0050').first()
        # 股票名字
        response['stock_name'] = stock.stock_name.rstrip()
        # 三天預測價格
        stock_three_days_predict = stock.three_days_predict
        three_days_predict = {
            'three_days_increase_one_percent': stock_three_days_predict.three_days_increase_one_percent,
            'three_days_increase_three_percent': stock_three_days_predict.three_days_increase_three_percent,
            'three_days_no_change': stock_three_days_predict.three_days_no_change,
            'three_days_decrease_one_percent': stock_three_days_predict.three_days_decrease_one_percent,
            'three_days_decrease_three_percent': stock_three_days_predict.three_days_decrease_three_percent
        }
        response['three_days_predict'] = three_days_predict

        # 五天預測價格
        stock_five_days_predict = stock.five_days_predict
        stock_five_days_predict_list = [
            stock_five_days_predict.future_first_day,
            stock_five_days_predict.future_second_day,
            stock_five_days_predict.future_third_day,
            stock_five_days_predict.future_forth_day,
            stock_five_days_predict.future_fifth_day
        ]
        # 抓出近30天股票資料
        line_chart_data = []
        stock_data = StockData.query.filter_by(stock_basic_info_id=stock.id).order_by(StockData.date.desc()).limit(30).all()
        for i in stock_data:
            time_stamp = int(i.date.strftime("%s")) * 1000
            data = [time_stamp, i.opening_price]
            line_chart_data.append(data)
        # 最新的交易日
        latest_stock_date = stock_data[0].date
        response['latest_date'] = latest_stock_date.strftime("%Y-%m-%d")
        # 處理五天預測價格的資料加入日期
        stock_date = latest_stock_date
        for i, element in enumerate(stock_five_days_predict_list):
            stock_date += timedelta(days=i + 1)
            time_stamp = int(stock_date.strftime("%s")) * 1000
            data = [time_stamp, element]
            line_chart_data.append(data)
        return line_chart_data




        return str(a)


        return response



    def post(self):

        return "123"


