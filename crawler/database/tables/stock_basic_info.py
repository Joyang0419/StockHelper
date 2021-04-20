from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from crawler.database import Base, session


class StockBasicInfo(Base):
    """table: 股票基本資訊"""
    __tablename__ = 'stock_basic_info'
    id = Column(Integer, primary_key=True)
    stock_symbol = Column(String(length=20), nullable=False, unique=True)
    stock_name = Column(String(length=45), nullable=False)
    industry_type_id = Column(Integer, ForeignKey('industry_types.id'), nullable=False)
    # relationship
    stock_basic_info_detail = relationship("StockBasicInfoDetail", uselist=False, back_populates="stock_basic_info")

    def __init__(self, stock_symbol,  stock_name, industry_type_id):
        """建構子"""
        self.stock_symbol = stock_symbol
        self.stock_name = stock_name
        self.industry_type_id = industry_type_id

    def update_attr(self, attr: dict):
        """動態調整欄位"""
        for key, item in attr.items():
            setattr(self, key, item)
        session.add(self)
        session.commit()

    def __repr__(self):
        """複印"""
        return "<StockBasicInfo(id={}, stock_symbol={}, stock_name={}, industry_type_id={})"\
            .format(self.id, self.stock_symbol, self.stock_name, self.industry_type_id)


