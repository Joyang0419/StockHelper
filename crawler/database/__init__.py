from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine("mysql+pymysql://root:stockhelper@172.18.0.101:3306/stockhelper", echo=True)
engine = create_engine("mysql+pymysql://root:stockhelper@35.215.134.213:3306/stockhelper", echo=True)
Base = declarative_base()

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

