from flask_restful import Resource, reqparse
from flask import request, current_app
from flask_login import login_user, login_required
# google oauth
from google.oauth2 import id_token
from google.auth.transport import requests
# models
from app.models.users import Users
# 處理圖檔儲存
import os
import urllib.request
# schemas
from ..schemas.users_schema import UsersSchema
from marshmallow import ValidationError


class UsersApi (Resource):

    def get(self):
        """
        確認使用者登入
        - 讀取前端的資料
        - 驗證google token
        """
        # 讀取前端的資料
        google_token = request.args.get('google_token', type=str)
        # google oauth client ID
        google_oauth_client_id = current_app.config['GOOGLE_OAUTH2_CLIENT_ID']

        # google驗證
        try:
            # Specify the GOOGLE_OAUTH2_CLIENT_ID of the app that accesses the backend:
            id_info = id_token.verify_oauth2_token(
                google_token,
                requests.Request(),
                google_oauth_client_id
            )
        except ValueError:
            # Invalid token
            return {
                'login_status': 0,
                'url': 'http://www.stockhelper.com.tw:8080/login'
            }
            raise ValueError('Invalid token')

        return {
            'login_status': 1,
        }

    def post(self):
        """
        使用者登入:
        - 讀取前端的資料
        - 驗證google token
        - 驗證資料
        - 回傳index url
        """
        # 上傳資料夾路徑: static/upload/users/<file>
        upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'users/')
        # google oauth client ID
        google_oauth_client_id = current_app.config['GOOGLE_OAUTH2_CLIENT_ID']
        # 讀取前端資料
        token = request.json['id_token']
        # google驗證
        try:
            # Specify the GOOGLE_OAUTH2_CLIENT_ID of the app that accesses the backend:
            id_info = id_token.verify_oauth2_token(
                token,
                requests.Request(),
                google_oauth_client_id
            )
            if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            # reference: https://developers.google.com/identity/sign-in/web/backend-auth
        except ValueError:
            # Invalid token
            raise ValueError('Invalid token')

        # 驗證資料
        data = {
            'username': id_info['name'],
            'email': id_info['email']
        }
        try:
           validated_data = UsersSchema().load(data)
        except ValidationError as error:
            print("ERROR: data is invalid")

        # email若不存在DB，新增；
        user = Users.query.filter_by(email=validated_data['email']).first()
        if user is None:
            user = Users.create(**validated_data)

        # 圖片進入資料庫
        image_url = id_info['picture']
        file_extension = 'jpg'
        file_name = str(user.id) + '.' + file_extension
        urllib.request.urlretrieve(image_url, os.path.join(upload_folder, file_name))

        return {'url': 'http://www.stockhelper.com.tw:8080/'}

