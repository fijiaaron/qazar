from flask import render_template
from cloudtestenvironment import app 


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	content = render_template('index.html')
	return content


@app.route('/landing')
@app.route('/landing.html')
def landing():
	content = render_template('landing.html')
	return content


@app.route('/details')
@app.route('/details.html')
def details():
	content = render_template("details.html")
	return content


@app.route('/register')
@app.route('/register.html')
def register():
	content = render_template('register.html')
	return content


@app.route('/order')
@app.route('/order.html')
def order():
	content = render_template('order.html')
	return content


@app.route('/payment/<method>', defaults={'method': 'paypal'})
def payment_method(method):
	content = render_template(payment, payment_method=method)
	return content


@app.route('/order/<status>')
def order_status(status):
	if (status == 'complete'):
		content = 'order complete'
	elif (status == 'error'):
		content = 'order error'
	else:
		content = order()
	return content


@app.route('/whitepaper')
@app.route('/whitepaper.html')
def whitepaper():
	content += "download whitepaper"
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