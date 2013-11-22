from flask import render_template, redirect, url_for, request, session
from cloudtestenvironment import app
<<<<<<< Updated upstream
from forms import RegistrationForm, ContactForm, PurchaseForm
from cloudtestenvironment.models import Customer
=======
from models import db, Customer, Contact
from time import strftime
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
	content = index()
	content += " payment page"
=======
	#content = index()
	#content += " payment page"
	purchase_form = PurchaseForm()
	content = render_template('payment.html', purchase_form=purchase_form)
>>>>>>> Stashed changes
	return content


@app.route('/payment/<method>', defaults={'method': 'paypal'})
def payment_method(method):
	content = payment()
	content += " method: " + method
	return content


@app.route('/payment/confirmation', methods=['POST'])
def payment_confirmation(status):
	content = payment()
	content += " status: " + status

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

#@app.route('/contact')
#@app.route('/contact.html')
#def contact(sent):
#	content = index()
#	content +=" contact form"
#	return content
@app.route('/register', methods=['GET', 'POST'])

def register():
	registration_form = RegistrationForm()
<<<<<<< Updated upstream
	customer = Customer()
	db_session.add(customer)
	db_session.commit()
	if not registration_form.validate_on_submit():
		return redirect()
	if request.registration_form['submit'] == "Tell Me More":
		customer.registered == False
		db_session.add(customer)
		db_session.commit()
		return redirect(url_for('details'))
	if request.registration_form['submit'] == "Sign Up":
		customer.registered == True
		db_session.add(customer)
		db_session.commit()
		return redirect(url_for('order'))


=======
	ref = request.referrer
	customer = Customer(
			name = registration_form.name.data,
			email = registration_form.email.data,
			phone = registration_form.phone.data,
			company = registration_form.company.data
		)		
	if registration_form.tell_me_more.data == True:
		customer.registered == False
		db.session.add(customer)
		db.session.commit()
		return redirect(url_for('details')) #TODO: we can't remove the anchor

	if registration_form.sign_up.data == True and registration_form.validate_on_submit():
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
>>>>>>> Stashed changes

@app.route('/contact')
@app.route('/contact.html')
def contact_message():
<<<<<<< Updated upstream
	content = render_template('contact_confirmation.html')
=======
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
	content = render_template('contact_confirmation.html', contact_form=contact_form)
>>>>>>> Stashed changes
	return content

with app.test_request_context():
	print "starting application"
	
