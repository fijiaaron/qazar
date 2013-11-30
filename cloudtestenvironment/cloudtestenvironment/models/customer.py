from cloudtestenvironment import db

class Customer(db.Model):
	__tablename__ = "customers"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(40))
	phone = db.Column(db.String(15))
	company = db.Column(db.String(40))
	registered = db.Column(db.Boolean)

	def __init__(self, name, email, phone=None, company=None, registered=False):
		self.name = name
		self.email = email
		self.phone = phone
		self.company = company
		self.registered = registered

