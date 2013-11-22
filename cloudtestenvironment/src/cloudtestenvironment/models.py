from flask.ext.sqlalchemy import SQLAlchemy
from cloudtestenvironment import app

db = SQLAlchemy(app)

<<<<<<< Updated upstream
class Registration(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(40))
	phone = db.Column(db.String(15))
	company = db.Column(db.String(40))

	def __init__(self, name, email, phone=None, company=None):
		self.name=name
		self.email=email
		self.phone=phone
		self.company=company

	def __repr__(self):
		return '<Registration id:%s>' % self.id


class Contact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(40))
	phone = db.Column(db.String(15))
	message = db.Column(db.String(500))

	def __init__(self, name, email, phone=None, company=None):
		self.name=name
		self.email=email
		self.phone=phone
		self.company=company

	def __repr__(self):
		return '<Contact id:%s>' % self.id

class Customer(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	address1 = db.Column(db.String(40))
	address2 = db.Column(db.String(40))
	country = db.Column(db.String(40))
	city = db.Column(db.String(40))
	state = db.Column(db.String(40))
	zipcode = db.Column(db.String(10))
	phone = db.Column(db.String(15))
	email = db.Column(db.String(40))
	registered = db.Column(db.Boolean, nullable=False)

	def __init__(self, name, address1, address2, country, city, state, zipcode, phone=None, email=None, registered=None):
		self.name=name
		self.address1=address1
		self.address2=address2
		self.country=country
		self.city=city
		self.state=state
		self.zipcode=zipcode
		self.phone=phone
		self.email=email
		self.registered=registered
	def __repr__(self):
		return '<User id:%s>' % self.id
=======
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
   	
>>>>>>> Stashed changes
