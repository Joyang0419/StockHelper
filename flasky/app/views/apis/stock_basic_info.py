from flask_restful import Resource, reqparse
from flask import request
# models
from app.models.stock_basic_info import StockBasicInfo


class StockBasicInfoApi(Resource):
    def get(self):
        b = StockBasicInfo.query.with_entities(StockBasicInfo.stock_name).all()
        return str(b[0][0])
        qq = []
        for i in b:
            qq.append(i.stock_symbol)
        return qq

    def post(self):
        """
        提供股票資訊
        - 提供股票名稱
        """
        # 讀取前端資料
        json_data = request.json
        """
        判斷交易動作
        - 買: 提供所有股票代號，股票名稱
        """
        # 交易動作: 買
        activity = json_data['activity']
        if activity == 'buy':
            data = StockBasicInfo.query.all()
            stock_symbol_list = []
            stock_name_list = []
            for i in data:
                stock_symbol_list.append(i.stock_symbol)
                stock_name_list.append(i.stock_name)
            response = {
                'stock_symbol_list': stock_symbol_list,
                'stock_name_list': stock_name_list
            }
            return response

