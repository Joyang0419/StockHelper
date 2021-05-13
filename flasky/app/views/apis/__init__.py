from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS
# 引入resource
from .users import UsersApi
from .stock_basic_info import StockBasicInfoApi


api_blueprint = Blueprint('api_blueprint', __name__)
# api灌入blueprint，為了使用url_prefix='/api'
api = Api(api_blueprint)
# api加入服務
api.add_resource(UsersApi, '/users')
api.add_resource(StockBasicInfoApi, '/stock_basic_info')
