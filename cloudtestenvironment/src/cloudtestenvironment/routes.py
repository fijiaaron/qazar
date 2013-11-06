from flask import render_template, redirect, url_for, request
from cloudtestenvironment import app
from models import db, Registration, Contact
from forms import RegistrationForm, ContactForm
from requests import post

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	content = render_template('index.html')
	return content


@app.route('/landing')
@app.route('/landing.html', methods=['GET'])
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
		registration = Registration(
			name = registration_form.name.data,
			email = registration_form.email.data,
			phone = registration_form.phone.data,
			company = registration_form.company.data
		)
		db.session.add(registration)
		db.session.commit()
		if registration_form.tell_me_more.data == True:
			return redirect(url_for('details', _anchor='registered')) #TODO: we can't remove the anchor
		if registration_form.sign_up.data == True:
			return redirect(url_for('order', _anchor='registered'))

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
	order = {}
	response = post("http://127.0.0.1:5050/provision", order)
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

@app.route('/contact', methods=['GET'])
@app.route('/contact.html', methods=['GET'])
def contact(sent):
	content = index()
	content +=" contact form"
	return content


@app.route('/contact', methods=['POST'])
@app.route('/contact.html', methods=['POST'])
def contact_message(sent):
	content = contact()
	content +=" message " + sent
	return content

with app.test_request_context():
	print "starting application"
	
