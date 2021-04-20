from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from crawler.database import Base, session


class IndustryTypes(Base):
    """table: 產業類別"""
    __tablename__ = 'industry_types'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=30), nullable=False, unique=True)
    # relationship
    stock_basic_info_aa = relationship("StockBasicInfo")

    def __init__(self, name):
        """建構子"""
        self.name = name

    def update_attr(self, attr: dict):
        """修改"""
        for key, item in attr.items():
            setattr(self, key, item)
        session.add(self)
        session.commit()

    def __repr__(self):
        """複印"""
        return "<IndustryTypes(id={}, name={})"\
            .format(self.id, self.name)

    @staticmethod
    def create(**kwargs):
        """新增"""
        obj = IndustryTypes(name=kwargs['name'])
        session.add(obj)
        session.commit()

