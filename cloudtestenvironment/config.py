#!flask/bin/python
import os

basedir = os.path.abspath(os.path.dirname(__file__)) 
db = os.path.join(basedir, 'cloudtestenvironment.db')

TESTING = True
if TESTING:
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
else:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
