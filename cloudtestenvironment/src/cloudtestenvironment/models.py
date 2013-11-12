from flask.ext.sqlalchemy import SQLAlchemy
from cloudtestenvironment import app

db = SQLAlchemy(app)

class Contact(db.Model):
<<<<<<< HEAD
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(40))
        email = db.Column(db.String(40))
        phone = db.Column(db.String(15))
        message = db.Column(db.String(500))

        def __init__(self, name, email, phone, message):
                self.name = name
                self.email = email
                self.phone = phone
                self.message = message

class Customer(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(40))
        email = db.Column(db.String(40))
        phone = db.Column(db.String(15))
        company = db.Column(db.String(40))
        registered = db.Column(db.Boolean)

        def __init__(self, name, email, phone, company, registered=False):
                self.name = name
                self.email = email
                self.phone = phone
                self.company = company
                self.registered = registered
=======
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(40))
	phone = db.Column(db.String(15))
	message = db.Column(db.String(500))

	def __init__(self, name, email, phone, message):
		self.name = name
		self.email = email
		self.phone = phone
		self.message = message

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(40))
	phone = db.Column(db.String(15))
	company = db.Column(db.String(40))
	registered = db.Column(db.Integer)

	def __init__(self, name, email, phone, company, registered=1):
		self.name = name
		self.email = email
		self.phone = phone
		self.company = company
		self.registered = registered

>>>>>>> 122b4757dcb3eda735f5971e7189c720bcfe71b0
