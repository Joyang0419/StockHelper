from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+pymysql://root:stockhelper@35.201.208.222:3306/stockhelper", echo=True)
Base = declarative_base()

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

