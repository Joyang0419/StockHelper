from flask import Blueprint
from flask_restful import Api
# 引入resource
from .users import Users

api_blueprint = Blueprint('api_blueprint', __name__)
# api灌入blueprint，為了使用url_prefix='/api'
api = Api(api_blueprint)
# api加入服務
api.add_resource(Users, '/users')