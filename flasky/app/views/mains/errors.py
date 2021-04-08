from flask import render_template
from . import mains


@mains.app_errorhandler(404)
def page_not_found(e):
    """狀態404: Not Found"""
    return render_template('404.html'), 404


@mains.app_errorhandler(500)
def internal_server_error(e):
    """狀態500: Internal Server Error"""
    return render_template('500.html'), 500
