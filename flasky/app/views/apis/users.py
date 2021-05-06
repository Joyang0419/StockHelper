from flask_restful import Resource, reqparse
from flask import request, current_app
# models
from app.models.users import Users
import pandas as pd
import os


class Users (Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        # 上傳資料夾路徑: static/upload/users/<file>
        upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'users/')
        data = request.form
        df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                           'mask': ['red', 'purple'],
                           'weapon': ['sai', 'bo staff']})
        df.to_csv(os.path.join(upload_folder, '123.txt'), index=False)
        return data

