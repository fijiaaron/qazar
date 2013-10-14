from flask import current_app, request
from app import app
from app.helper import Helper

class BaseController():
    def __init__(self):
        self.redirector = Helper()
    
    @app.before_request
    def log_request():
        import logging
        logging.basicConfig(filename="error.log", level=logging.DEBUG)



