from flask import Flask
<<<<<<< HEAD:cloudtestenvironment/src/cloudtestenvironment/__init__.py


app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')



from cloudtestenvironment import routes
from cloudtestenvironment import models

models.db.create_all()
=======
app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

import models
import routes
>>>>>>> 07ce18808c46ac0b007e0a0de7997e4f5127cfd0:cloudtestenvironment/cloudtestenvironment/__init__.py
