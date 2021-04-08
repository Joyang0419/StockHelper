from flask import render_template
from . import mains
from app import db


@mains.route('/')
def index():
    return "index"
