import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = os.path.join(basedir, 'cloudtestenvironment.db')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
<<<<<<< HEAD:cloudtestenvironment/src/config.py
=======

>>>>>>> 07ce18808c46ac0b007e0a0de7997e4f5127cfd0:cloudtestenvironment/config.py
