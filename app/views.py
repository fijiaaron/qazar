from flask import render_template, flash, redirect
from app import app
from forms import Register, Payment

#@app.route('/', defaults={'path': ''})
#@app.route('/<path:path>')
#def controller(path):
    #return render_template(path)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/landing')
def landing():
    return render_template("landing.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/details')
def details():
    return render_template("details.html")

@app.route('/register', methods = ['GET', 'POST'])
def register(request):
    form = Register(request.form)
    if form.validate_on_submit() and request.form['submit'] == 'Credit Card':
        flash('Thank you ' + form.name.data + '. Redirecting to payment page.')
        return redirect('/payment')
    elif form.validate_on_submit():
        flash('Thank you ' + form.name.data + '. Redirecting to paypal.')
        return redirect('https://www.paypal.com/cgi-bin/webscr')
    return render_template('register.html', title = 'Register', form = form)

@app.route('/contact_confirmation')
def contact_confirmation():
    return render_template("contact_confirmation.html")

@app.route('/payment')
def payment():
    return render_template("payment.html")

@app.route('/creditcard_form', methods= ['GET', 'POST'])
def creditcard_form():
    form = Payment()
    if form.validate_on_submit():
        flash('Thank you for your payment. Redirecting to confirmation.')
        return redirect('/payment_confirmation')
    return render_template('creditcard_form.html', title = 'Credit Card Form', form = form)

@app.route('/payment_confirmation')
def payment_confirmation():
    return render_template('payment_confirmation.html')

@app.route('/paypal')
def paypal():
    return render_template("paypal.html")

@app.route('/creditcard')
def creditcard():
    return render_template("creditcard.html")

#Footer
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/login')
def login():
    return render_template("login.html")
