from cloudtestenvironment import db
from cloudtestenvironment.models import Customer

def setup():
	print
	print "recreating database tables"
	print(db)
	db.drop_all()
	db.create_all()

def test_create_customer():
	customer = Customer("John Doe", "johnd@example.com")
	assert customer.name == "John Doe"
	assert customer.email == "johnd@example.com"

def test_save_customer():
	customer = Customer("John Doe", "johnd@example.com")
	db.session.add(customer)
	db.session.commit()

	retrieved = Customer.query.first();
	assert customer.name == retrieved.name
	assert customer.email == retrieved.email
