from flask import render_template, redirect, url_for, request, session
from forms import RegistrationForm, ContactForm, PurchaseForm
from cloudtestenvironment import app
from models import db, Customer, Contact
from requests import post
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

	if registration_form.tell_me_more.data == True:
			return redirect(url_for('details')) #TODO: we can't remove the anchor
	if registration_form.sign_up.data == True:
		if registration_form.validate_on_submit():
			return redirect('register')

	contact_form = ContactForm()

	if contact_form.send.data == True:
		if contact_form.validate_on_submit():
			return redirect('contact')

	content = render_template('landing.html', registration_form=registration_form, contact_form=contact_form)
	return content

@app.route('/order', methods=['GET'])
def order():
	purchase_form = PurchaseForm()

	content = render_template('order.html', purchase_form=purchase_form)
	return content

@app.route('/order', methods=['POST'])
def order_submit():
	purchase_form = PurchaseForm()
		#TODO: save cc form
	if purchase_form.submit.data == True:
			return redirect('https://www.paypal.com/cgi-bin/webscr')
	content = render_template('order.html', purchase_form=purchase_form)
	return content

@app.route('/payment')
@app.route('/payment')
def payment():
	#content = index()
	#content += " payment page"
	content = render_template('payment.html')
	return content

@app.route('/payment/<method>', defaults={'method': 'paypal'})
def payment_method(method):
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
	registration_form = RegistrationForm()

	content = render_template('details.html', registration_form=registration_form)
	return content

@app.route('/details')
@app.route('/details', methods=['POST'])
def details_submit():

	registration_form = RegistrationForm()

	if registration_form.sign_up.data == True:
		if registration_form.validate_on_submit():
			return redirect(url_for('order'))

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

#@app.route('/contact')
#@app.route('/contact.html')
#def contact(sent):
#	content = index()
#	content +=" contact form"
#	return content

@app.route('/register', methods=['GET', 'POST'])
def register():
	registration_form = RegistrationForm()
	ref = request.referrer
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
		return redirect(ref)
		
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

@app.route('/contact')
@app.route('/contact.html')
def contact_message():
	contact_form = ContactForm()
	ref = request.referrer
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
		return redirect(ref)
	else:
		db.session.add(customer)
		db.session.commit()
		return "message sent"
	content = render_template('contact_confirmation.html')
	return content

with app.test_request_context():
	print "starting application"