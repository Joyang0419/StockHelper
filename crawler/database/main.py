from crawler.database import Base, engine
# 引入要新增的table
from tables.industry_types import IndustryTypes
from tables.stock_basic_info import StockBasicInfo
from tables.stock_basic_info_detail import StockBasicInfoDetail


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    IndustryTypes.create(name='123')
