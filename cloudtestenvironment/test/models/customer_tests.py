import unittest
from cloudtestenvironment.models import Customer

class CustomerTests(unittest.TestCase):
	def testCustomerCreation(self):
			name = "My Name"
			email = "me@example.com"

			customer = Customer(name, email)
			self.assertEqual(customer.name, name)
			self.assertEqual(customer.email, email)

if __name__ == '__main__':
	unittest.main()