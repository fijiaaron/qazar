from flask import render_template, redirect, url_for, request, session
from cloudtestenvironment import app, bcrypt
from models import db, Customer
from forms import RegistrationForm, ContactForm
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

	if registration_form.validate_on_submit():
		#TODO: save registration
		customer = Customer(
			name = registration_form.name.data,
			email = registration_form.email.data,
			phone = registration_form.phone.data,
			company = registration_form.company.data
		)
		if registration_form.tell_me_more.data == True:
			db.session.add(customer)
			db.session.commit()
			return redirect(url_for('details', _anchor='registered')) #TODO: we can't remove the anchor
		if registration_form.sign_up.data == True:
			customer.registered = 1
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
		return "message sent"
	if contact_form.send.data == True:
		if contact_form.validate_on_submit():
			return redirect('contact')

	content = render_template('landing.html', registration_form=registration_form, contact_form=contact_form)
	return content

@app.route('/order')
@app.route('/order.html')
def order():
	content = render_template('order.html')
	return content


@app.route('/payment')
@app.route('/payment.html')
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
@app.route('/details.html')
def details():
	content = render_template("details.html")
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


@app.route('/contact')
@app.route('/contact.html')
def contact_message():
	content = render_template('contact_confirmation.html')
	return content

with app.test_request_context():
	print "starting application"
	
