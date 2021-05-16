from flask_restful import Resource, reqparse, current_app
# models
from app.models.stock_basic_info import StockBasicInfo
from app.models.stock_data import StockData
# others
from datetime import datetime


class StockDataApi(Resource):
    def get(self):
        stock = StockBasicInfo.query.filter_by(stock_symbol='0050').first()
        stock_data = StockData.query.filter_by(stock_basic_info_id=stock.id).order_by(StockData.date).all()
        stock_data_list = []

        dt_obj = datetime.strptime('20.12.2016 09:38:42,76',
                                   '%d.%m.%Y %H:%M:%S,%f')
        for i in stock_data:
            data = [
                int(i.date.strftime("%s")) * 1000 + 28800000,
                i.opening_price,
                i.highest_price,
                i.lowest_price,
                i.closing_price,
                i.volume
            ]
            stock_data_list.append(data)
        return stock_data_list

        #
        # return str(stock_data.opening_price)
        # return stock.stock_symbol
        return "123"

    # int(datetime.datetime.strptime('01/12/2011', '%d/%m/%Y').strftime("%s"))

    # stock_data = stock.stock_data[0]
    # trade_date = int(stock_data.date.strftime("%s"))
