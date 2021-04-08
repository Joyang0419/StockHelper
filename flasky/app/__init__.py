from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
# 匯入config.py
from config import config


# 工具(尚未初始化)
db = SQLAlchemy()
mail = Mail()


def create_app(config_name):
    """flask factory"""
    app = Flask(__name__)
    # 將config.py內定義的組態類別，其所儲存的組態設定直接匯入App
    app.config.from_object(config[config_name])
    print(app.config['DEBUG'])
    # print(config[config_name].DEBUG)
    # App初始化工具，使用init_app()
    config[config_name].init_app(app)
    db.init_app(app)
    mail.init_app(app)
    """
    routes: 註冊blueprints
    網站:
    - mains
    - websites
    - admins
    APIs 
    """
    # 主要網站
    # mains
    from .views.mains import mains as mains_blueprint
    app.register_blueprint(mains_blueprint)
    # websites
    from .views.mains.websites import websites as websites_blueprint
    app.register_blueprint(websites_blueprint)
    # admins
    from .views.mains.admins import admins as admins_blueprint
    app.register_blueprint(admins_blueprint)
    # API
    from .views.APIs import apis as apis_blueprint
    app.register_blueprint(apis_blueprint)

    return app

