import unittest
from cloudtestenvironment import db
from cloudtestenvironment.models import Customer

class CustomerTests(unittest.TestCase):
	def testCustomerCreation(self):
		name = "My Name"
		email = "me@example.com"

		customer = Customer(name, email)

		self.assertEqual(customer.name, name)
		self.assertEqual(customer.email, email)

		db.session.add(customer)
		db.session.commit()

if __name__ == '__main__':
	unittest.main()