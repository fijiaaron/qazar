import paypalrestsdk
import paypalconfig

class PaypalPaymentProcessor():
	"""
	"""
	def __init__(self):
		"""
		"""
		paypalrestsdk.configure({
                   "mode": paypalconfig.PAYPAL_MODE,
		   "client_id": paypalconfig.PAYPAL_CLIENT_ID,
		   "client_secret": paypalconfig.PAYPAL_CLIENT_SECRET
		})

	def make_payment(self, payment_info, order):
		"""
		"""
		payment = paypalrestsdk.Payment({
			"intent": "sale",
			"payer": {"payment_method": "paypal"},
			"redirect_urls": {
				"return_url": "http://cloudtestenvironment.com/payment/confirmation",
				"cancel_url": "http://cloudtestenvironment.com"
            },
			"transactions": [{
			    "item_list": {
					"items": [{
						"name": "Test Environment",
						"sku": "Test Environment",
						"price": "0.99",
						"currency": "USD",
						"quantity": 1
					}]
				},
			    "amount": {
				    "total": "0.99",
					"currency": "USD"
				}, 
                            "description": "Test transaction."
			}]
		})
		
		if payment.create():
			print("Payment[%s] created successfully"%(payment.id))
		else:
			print("Error while creating payment:")
			print payment.error
		
		# Once a payment is created, you want to look for the 
		# approval_url in the response. An example response
		# can be found at:
		# https://developer.paypal.com/webapps/developer/docs/
		# integration/web/accept-paypal-payment/
		# You direct the customer to the approval_url.  When the 
		# customer approves the payment, then the customer is 
		# redirected to the return_url found above with token 
		# and PayerID parameters appended to the return_url.  
		# In our case, this means that the customer will be 
		# redirected to a url that looks like: 
		# http://cloudtestenvironment.com/payment/confirmation/
		# ?token=EC-65C09643656060905&PayerID=NL8QJGEAPYFFA.
		# This PayerID is needed for the payment to be executed
		# in the following manner with the paypalrestsdk:
		# payment.execute({"payer_id": PayerID})
		
		return payment
