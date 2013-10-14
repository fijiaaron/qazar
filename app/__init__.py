from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
<<<<<<< HEAD
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
=======

from app.basecontroller import BaseController

test = BaseController()

>>>>>>> 54d81636c49ef37f391f46c65a1f8a2f28ac76f4
