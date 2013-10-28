from flask import Flask

app = Flask(__name__)

from app.basecontroller import BaseController

test = BaseController()
