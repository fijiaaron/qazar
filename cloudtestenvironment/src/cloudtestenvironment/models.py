from flask.ext.sqlalchemy import SQLAlchemy
from cloudtestenvironment import app

db = SQLAlchemy(app)

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(40))
	phone = db.Column(db.String(15))
	company = db.Column(db.String(40))
	registered = db.Column(db.Boolean)

	# relational patterns
	address = db.relationship('Address')
	user = db.relationship('User')
	account = db.relationship('Account')
	message = db.relationship('Message')
	order = db.relationship('Order')

	def __init__(self, name, email, phone, company, registered=False):
		self.name = name
		self.email = email
		self.phone = phone
		self.company = company
		self.registered = registered

<<<<<<< HEAD
<<<<<<< HEAD
	def __repr__(self):
		return '<Contact id:%s>' % self.id

class Customer(db.Model):
	__tablename__ = 'users'
=======
class Address(db.Model):
>>>>>>> 5ad3af6b9a7d462001011edaa1c356638fd2893b
	id = db.Column(db.Integer, primary_key=True)
	address1 = db.Column(db.String(40))
	address2 = db.Column(db.String(40))
	city = db.Column(db.String(40))
	state = db.Column(db.String(40))
<<<<<<< HEAD
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
>>>>>>> 122b4757dcb3eda735f5971e7189c720bcfe71b0
=======
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

>>>>>>> 5ad3af6b9a7d462001011edaa1c356638fd2893b
