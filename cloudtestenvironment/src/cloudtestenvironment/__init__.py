from flask import Flask
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')

bcrypt = Bcrypt(app)

from cloudtestenvironment import routes
from cloudtestenvironment import models

models.db.create_all()
