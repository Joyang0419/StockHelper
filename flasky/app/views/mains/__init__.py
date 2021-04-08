from flask import Blueprint

mains = Blueprint('mains', __name__)

# 匯入routes
from . import errors, index
