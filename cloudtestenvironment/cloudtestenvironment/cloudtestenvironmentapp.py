from flaskless_models import Payment

class CloudTestEnvironmentApp():

	def __init__(self, session=None, payment_processor=None):
		self.session = session
		self.payment_processor = payment_processor

	def register(self, customer):
		"""
		Args:
			customer: A Customer Model instance.
		"""
		if customer_info.validate():
			self.session.add(customer)
			self.session.commit()
		else:
			raise ValidationError("Info Not Validated.") 

	def order(self, order):
		"""
		Args:
			order: An Order Model instance.
		"""
		self.session.add(order)
		self.session.commit()

	def purchase(self, payment_info, order):
		"""
		Args:
			payment_info: A Dictionary instance.
			order: A Order Model instance.
		"""
		payment = self.payment_processor.make_payment(payment_info, order)
		self.session.add(
		    Payment(
                order_id = order.id,
				payment_on = payment.create_time,
				payment_method = payment.payer.payment_method,
				payment_status = payment.state
			)
		)
		self.session.commit()
