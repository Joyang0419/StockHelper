from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_login import LoginManager
# 匯入config.py
from config import config


# 工具(尚未初始化)
db = SQLAlchemy()
mail = Mail()
api = Api()
cors = CORS()
login_manager = LoginManager()


def create_app(config_name):
    """flask factory"""
    app = Flask(__name__)
    # 將config.py內定義的組態類別，其所儲存的組態設定直接匯入App
    app.config.from_object(config[config_name])
    # print(config[config_name].DEBUG)
    # App初始化工具，使用init_app()
    config[config_name].init_app(app)
    db.init_app(app)
    mail.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "http://www.stockhelper.com.tw:8080"}})
    # 引入api
    from app.views.apis import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

