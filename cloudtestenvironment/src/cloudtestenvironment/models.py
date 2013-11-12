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
	addresses = relationship('Address')
	users = relationship('User')
	accounts = relationship('Account')
	messages = relationship('Message')
	orders = relationship('Order')

	def __init__(self, name, email, phone, company, registered=0):
		self.name = name
		self.email = email
		self.phone = phone
		self.company = company
		self.registered = registered

class Address(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	address1 = db.Column(db.String(40))
	address2 = db.Column(db.String(40))
	city = db.Column(db.String(40))
	state = db.Column(db.String(40))
	country = db.Column(db.String(40))
	zip_code = db.Column(db.String(10))
	address_type = db.Column(db.String(40))
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

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(40))
	password_hash = db.Column(db.String(40))
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

	def __init__(self, username, password_hash, customer_id):
		self.username = username
		self.password_hash = password_hash
		self.customer_id = customer_id

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	balance = db.Column(db.Decimal(2))
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

	def __init__(self, balance, customer_id):
		self.balance = balance
		self.customer_id = customer_id

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	message = db.Column(db.String())
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

	def __init__(self, message, customer_id):
		self.message = message
		self.customer_id = customer_id

class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
	environment_id = db.Column(db.Integer, db.ForeignKey('environment.id'))
	payment = relationship('Payment')

	def __init__(self, customer_id, environment_id):
		self.customer_id = customer_id
		self.environment_id = environment_id

class Environment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String())
	order = relationship('Order')

	def __init__(self, description):
		self.description = description

class Payment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	amount = db.Column(db.Decimal(2))
	order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

	def __init__(self, amount, order_id):
		self.amount = amount
		self.order_id = order_id


