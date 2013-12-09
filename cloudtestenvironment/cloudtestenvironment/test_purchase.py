from cloudtestenvironmentapp import CloudTestEnvironmentApp
from paypalpaymentprocessor import PaypalPaymentProcessor
from flaskless_models import Order, Payment
from database import db_session, init_db
import unittest

class TestCloudTestEnvironmentAppFunctions(unittest.TestCase):
	def setUp(self):
		payment_processor = PaypalPaymentProcessor()
		self.app = CloudTestEnvironmentApp(db_session, payment_processor)
		init_db()
		self.customer_info = {}
		self.order = Order()

	def test_purchase(self):
		self.app.purchase(self.customer_info, self.order)
		payment = self.app.session.query(Payment).first()
		self.assertEqual(payment.order_id, self.order.id)
		self.assertEqual(payment.payment_method, "paypal")
		self.assertEqual(payment.payment_status, "created")

if __name__ == '__main__':
    unittest.main()



