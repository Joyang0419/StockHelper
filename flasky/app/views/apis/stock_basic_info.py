from flask_restful import Resource, reqparse
from flask import request
# models
from app.models.users import Users
from app.models.stock_basic_info import StockBasicInfo
from app.models.trade_records import TradeRecords


class StockBasicInfoApi(Resource):
    def get(self):
        user = Users.query.filter_by(email='joyang0419@gmail.com').first()
        user_trade_records = TradeRecords
        return str(user_trade_records)


    def post(self):
        """
        提供股票資訊
        - 提供股票名稱
        """
        # 讀取前端資料
        json_data = request.json
        """
        - 判斷執行事項:
            - 查詢資料
            - 提交表單
        """
        if json_data['action'] == 'submit':
            user = Users.query.filter_by(email=json_data['user_email']).first()
            trade_record = TradeRecords(**json_data['form'])
            # 利用relationship去新增Post
            user.create_trade_record(trade_record)
            return "交易成功"
        elif json_data['action'] == 'get_stock_name':
            activity = json_data['activity']
            stock = StockBasicInfo.query.filter_by(stock_symbol=json_data['stock_symbol']).first()
            if stock is None:
                return None
            return {
                'stock_name': stock.stock_name,
                'stock_basic_info_id': stock.id
            }
        elif json_data['action'] == 'get_stock_symbol_list':
            user = Users.query.filter_by(email=json_data['user_email']).first()
            user_trade_records = user.trade_records.group_by(TradeRecords.stock_basic_info_id)
            return "123"
            return str(user_trade_records)


