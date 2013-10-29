from flask.ext.sqlalchemy import SQLAlchemy
from cloudtestenvironment import app

db = SQLAlchemy(app)

class Registration(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(40))
	phone = db.Column(db.String(15))
	company = db.Column(db.String(40))

	def __init__(self, name, email, phone=None, company=None):
		self.name = name
		self.email = email
		self.phone = phone
		self.company = company

	def __repr__(self):
		return '<Registration id:%s>' % self.id


class Contact(db.Model):
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
