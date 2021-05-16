from app import db
from .db_abstract import DBAbstract


class StockBasicInfo(DBAbstract):
    """table: 股票基本資訊"""
    __tablename__ = 'stock_basic_info'
    id = db.Column(db.Integer, primary_key=True)
    stock_symbol = db.Column(db.String(20), nullable=False, unique=True)
    stock_name = db.Column(db.String(60), nullable=False)
    # relationship
    # stock_basic_info: trade_records = one : many
    trade_records = db.relationship('TradeRecords', backref='stock_basic_info', lazy=True)
    # stock_basic_info: stock_data = one : many
    stock_data = db.relationship('StockData', backref='stock_basic_info', lazy=True)
