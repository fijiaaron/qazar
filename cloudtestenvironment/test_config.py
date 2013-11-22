import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = os.path.join(basedir, 'cloudtestenvironment.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

database = {
	'uri' : SQLALCHEMY_DATABASE_URI
	'secret_key' : SECRET_KEY
	'csrf_enabled' : CSRF_ENABLED
}

paypal = {
	'account' : 'foo@example.com'
	'password' : 'secret'
}