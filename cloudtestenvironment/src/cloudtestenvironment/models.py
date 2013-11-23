from flask.ext.sqlalchemy import SQLAlchemy
from cloudtestenvironment import app

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(40))
	password_hash = db.Column(db.String(255))
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

	def __init__(self, username, password_hash, customer_id):
		self.username = username
		self.password_hash = password_hash
		self.customer_id = customer_id

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	balance = db.Column(db.Numeric(2))
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

	def __init__(self, balance, customer_id):
		self.balance = balance
		self.customer_id = customer_id

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	message = db.Column(db.String(255))
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

	def __init__(self, message, customer_id):
		self.message = message
		self.customer_id = customer_id

class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
	total_amount = db.Column(db.Numeric(2))
	discount = db.Column(db.Numeric(2))
	order_created = db.Column(db.String(40))
	order_fulfilled = db.Column(db.String(40))
	order_items = db.relationship('OrderItems')
	payment = db.relationship('Payment')

	def __init__(self, customer_id, total_amount, discount, order_created, order_fulfilled):
		self.customer_id = customer_id
		self.total_amount = total_amount
		self.discount = discount
		self.order_created = order_created
		self.order_fulfilled = order_fulfilled

class OrderItems(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
	description = db.Column(db.String(255))
	price = db.Column(db.Numeric(2))
	discount = db.Column(db.Numeric(2))
	quantity = db.Column(db.Integer)

	def __init__(self, order_id, description, price, discount, quantity):
		self.order_id = order_id
		self.description = description
		self.price = price
		self.discount = discount
		self.quantity = quantity

class Environment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(255))

	def __init__(self, description):
		self.description = description

class Payment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
	amount = db.Column(db.Numeric(2))
	payment_on = db.Column(db.String(40))
	payment_method = db.Column(db.String(40))
	def __init__(self, order_id, amount, payment_on, payment_method):
		self.order_id = order_id
		self.amount = amount
		self.payment_on = payment_on
		self.payment_method = payment_method


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