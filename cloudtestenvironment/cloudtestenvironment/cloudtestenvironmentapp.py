from json import dumps
from wtforms.validators import ValidationError
from flaskless_models import Customer, Order

class CloudTestEnvironmentApp():

	def __init__(self, session):
		self.session = session

	def register(self, customer_info):
		"""
		Args:
			customer_info: A RegistrationForm Form instance.
		"""
		customer = Customer(
			name = customer_info.name.data,
			email = customer_info.email.data,
			phone = customer_info.phone.data,
			company = customer_info.company.data
		)
		if customer_info.validate():
			self.session.add(customer)
			self.session.commit()
		else:
			raise ValidationError("Info Not Validated.") 
		return customer

	def order(self, order):
		"""
		Args:
			order: A Order Model instance.
			customer: A Customer Model instance.
		"""
		#order = Order(
			#customer_id = customer.id,
            #order_items = dumps([item.data for item in order_info.order_items]),
			#order_location = order_info.order_location.data
		#)
		#if order_info.validate():
		self.session.add(order)
		self.session.commit()
		#else:
			#raise ValidationError("Info Not Validated.")
		#return order

	def purchase(self, payment_info, order):
		"""
		Args:
			payment_info: A PurchaseForm Form instance.
			order: A Order Model instance.
		"""
		payment_status = Payment(
			order_id = order.id,
			payment_method = dumps({field.name: field.data for field in payment_info})
		)

