from flask import render_template, redirect, url_for, request
from cloudtestenvironment import app
from forms import RegistrationForm, ContactForm

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
			return redirect(url_for('order'))

	contact_form = ContactForm()


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
	content = index()
	content += " payment page"
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
	