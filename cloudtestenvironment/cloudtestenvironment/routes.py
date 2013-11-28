from flask import render_template, redirect, url_for, request, session
from forms import RegistrationForm, ContactForm, PaypalForm, CreditCardForm, OrderForm
from cloudtestenvironment import app
from models import db, Customer, Order, OrderItems
from time import strftime


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	content = render_template('index.html')
	return content

@app.route('/landing')
@app.route('/landing', methods=['GET'])
def landing():
	registration_form=RegistrationForm()
	contact_form=ContactForm()

	content = render_template('landing.html', registration_form=registration_form, contact_form=contact_form)
	return content

@app.route('/landing', methods=['POST'])
def landing_submit():
	registration_form = RegistrationForm() 
	#TODO: save registration

	customer = Customer("Aaron Evans", "aarone@one-shore.com", "425-242-4304", "One Shore Inc")

	if registration_form.tell_me_more.data == True:
		return redirect(url_for('details')) #TODO: we can't remove the anchor
	
	if registration_form.sign_up.data == True:

		if registration_form.validate_on_submit():

			return redirect('register')


			return redirect(url_for('register'), code=307)


	contact_form = ContactForm()

	if registration_form.validate_on_submit():
		#TODO: save registration
		customer = Customer(
			name = registration_form.name.data,
			email = registration_form.email.data,
			phone = registration_form.phone.data,
			company = registration_form.company.data
		)
		if registration_form.tell_me_more.data == True:
			customer.registered = 0
			db.session.add(customer)
			db.session.commit()
			return redirect(url_for('details', _anchor='registered')) #TODO: we can't remove the anchor
		if registration_form.sign_up.data == True:
			db.session.add(customer)
			db.session.commit()
			return redirect(url_for('order', _anchor='registered'))
	else:
		session['name'] = registration_form.name.data
		session['email'] = registration_form.email.data
		session['phone'] = registration_form.phone.data
		session['company'] = registration_form.company.data


	contact_form = ContactForm()
	if contact_form.validate_on_submit():
		# TODO: save message
		contact = Contact(
			name = contact_form.name.data,
			email = contact_form.email.data,
			phone = contact_form.phone.data,
			message = contact_form.message.data
		)
		db.session.add(contact)
		db.session.commit()
		return "message sent"

	if contact_form.send.data == True:
		if contact_form.validate_on_submit():
			return redirect(url_for('contact'))

	content = render_template('landing.html', registration_form=registration_form, contact_form=contact_form)
	return content

@app.route('/order', methods=['GET'])
def order():
	paypal_form = PaypalForm()
	credit_card_form = CreditCardForm()
	order_form = OrderForm()
	content = render_template('order.html', paypal_form=paypal_form, credit_card_form=credit_card_form, order_form=order_form)
	return content

@app.route('/order', methods=['POST'])
def order_submit():
	paypal_form = PaypalForm()
	order_form = OrderForm()
	credit_card_form = CreditCardForm()
	order = Order(
		customer_id = 1,
		total_amount = 1.99, 
		discount = 0.99,
		order_created = strftime("%c"),
		order_fulfilled = strftime("%c")
	)

	order_items = OrderItems(
		order_id = order.id,
		description = "{'enviroment': {'nodes': [{'apps': ['jenkins', 'bugzilla', 'fitnesse', 'selenium'], 'memory': '1GB', 'os': 'ubuntu 12.04 LTS', 'name': 'tools', 'description': 'host build automation and test management tools'}, {'memory': '2GB', 'os': 'ubuntu 12.04 LTS', 'name': 'web', 'dependencies': [{'python': '2.7'}, {'mysql': '5.5'}], 'description': 'deploy python webapp for testing'}]}}",		
        price = 99.99,
		discount = 0.00,
		quantity = 1
	)
	db.session.add(order)
	db.session.add(order_items)
	db.session.commit()
		#TODO: save cc form
	if purchase_form.submit.data == True:
		return redirect('https://www.paypal.com/cgi-bin/webscr')
	content = render_template('order.html', paypal_form=paypal_form, credit_card_form=credit_card_form, order_form=order_form)
	return content

@app.route('/payment')
@app.route('/payment.html')
def payment():

	content = render_template('payment.html')

	#content = index()
	#content += " payment page"
	purchase_form = PurchaseForm()
	content = render_template('payment.html', purchase_form=purchase_form)

	#content = index()
	#content += " payment page"
	content = render_template('payment.html')

	return content

@app.route('/payment/<method>', defaults={'method': 'paypal'})
def payment_method(method):

	content = render_template('creditcard.html')
	return content


	#content = payment()
	#content += " method: " + method
	content = render_template('creditcard.html')
	return content

@app.route('/payment/confirmation', methods=['GET','POST'])
def payment_confirmation():
	for_provisioner = {
		'description': 'jenkins',
		'time': strftime("%c"),
		'ip_address': request.remote_addr,
		'customer': 'Johnny Test'
	}
	response = post("http://127.0.0.1:5050/provision", params=for_provisioner)
	content = render_template('payment_confirmation.html')
	return content

	#content = payment()
	#content += " status: " + status


@app.route('/details')
@app.route('/details', methods=['GET'])
def details():

	registration_form=RegistrationForm()
	contact_form=ContactForm()

	content = render_template("details.html", registration_form=registration_form, contact_form=contact_form)
	return content

@app.route('/details')
@app.route('/details', methods=['POST'])
def details_submit():

	registration_form = RegistrationForm()
		
	if registration_form.sign_up.data == True:
		if registration_form.validate_on_submit():

			return redirect(url_for('register'), code=307)

			return redirect('register')


	content = render_template('details.html', registration_form=registration_form)
	return content

@app.route('/whitepaper')
@app.route('/whitepaper.html')
def whitepaper():
	content = index()
	content += " whitepaper page"
	return content

@app.route('/whitepaper/download')
@app.route('/whitepaper/download.html')
def whitepaper_download(register):
	content = whitepaper()
	content += " download " + register
	return content

@app.route('/register', methods=['GET', 'POST'])

def register():
	registration_form = RegistrationForm()

	customer = Customer(
		name = registration_form.name.data,
		email = registration_form.email.data,
		phone = registration_form.phone.data,
		company = registration_form.company.data
	)

	if not registration_form.validate_on_submit():
		customer.registered == False
		db.session.add(customer)
		db.session.commit()
		return redirect(url_for('landing')) #TODO: Redirect to referrer page	

	if registration_form.tell_me_more.data == True:
		customer.registered == False
		db.session.add(customer)
		db.session.commit()
		return redirect(url_for('details', _anchor='registered')) #TODO: we can't remove the anchor

	if registration_form.sign_up.data == True:
		customer.registered == True
		db.session.add(customer)
		db.session.commit()
		return redirect(url_for('order', _anchor='registered'))
	else:
		customer.registered == False
		db.session.add(customer)
		db.session.commit()
		return redirect(ref or url_for('landing'))
	content = render_template('landing.html', registration_form=registration_form, contact_form=contact_form)
	return content

@app.route('/contact')
@app.route('/contact.html')
def contact_message():
	contact_form = ContactForm()
	customer = Customer(
		name = contact_form.name.data,
		email = contact_form.email.data,
		phone = contact_form.phone.data,
		company = contact_form.company.data
	)
	if not contact_form.validate_on_submit():
		customer.registered == False
		db.session.add(customer)
		db.session.commit()
		return redirect(request.referrer)
	else:
		db.session.add(customer)
		db.session.commit()
		return "message sent"
	content = render_template('contact_confirmation.html', contact_form=contact_form)
	return content


with app.test_request_context():
	print "starting application"
