from flask.ext.sqlalchemy import SQLAlchemy
from cloudtestenvironment import app

db = SQLAlchemy(app)

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(40))
	phone = db.Column(db.String(15))
	company = db.Column(db.String(40))
	registered = db.Column(db.Integer)
	addresses = relationship("Address")

	def __init__(self, name, email, phone, company, registered=0):
		self.name = name
		self.email = email
		self.phone = phone
		self.company = company
		self.registered = registered

class Address(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	address1 = db.Column()
	address2 = db.Column()
	city = db.Column()
	state = db.Column()
	country = db.Column()
	zip_code = db.Column()
	address_type = db.Column()
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

	def __init__(self, address1, address2, city, state, country, 
				zip_code, address_type, customer_id):
		self.address1 = address1
		self.address2 = address2
		self.city = city
		self.state = state
		self.country = country
		self.zip_code = zip_code
		self.address_type = address_type
		self.customer_id = customer_id

