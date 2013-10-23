from flask import render_template, redirect, request
from app import app
from forms import Register, Payment

class Helper():
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template("index.html")

    @app.route('/landing', methods = ['GET', 'POST'])
    def landing():
        form = Register()
        if request.path == "/landing#contact":
            form = Contact()
        if request.method == 'POST':
            if request.form['submit'] == "Learn More":
                return redirect('/details')
            if form.validate_on_submit() and request.form['submit'] == "Sign Up":
                return redirect('/order')
            if form.validate_on_submit() and request.form['submit'] == "Send":
                return redirect('/contact_confirmation')
        return render_template("landing.html",
                title = 'Landing',
                form = form)
       

    @app.route('/landing#contact', methods = ['GET', 'POST'])
    def contact():
        contact = Contact()
        if contact.validate_on_submit():
            return redirect('/contact_confirmation')
        return render_template("contact_form.html", title='Contact Form', form=contact)

    @app.route('/contact_form', methods = ['GET', 'POST'])
    def contact_form():
        contact = Contact()
        if request.method == 'POST':
            if contact.validate_on_submit():
                return redirect('/contact_confirmation')
        return render_template("contact_form.html", title='Contact Form', form=contact)

    @app.route('/details')
    def details():
        return render_template("details.html")

    @app.route('/landing#register', methods = ['GET', 'POST'])
    def register():
        registration = Register()
        if request.method == 'POST':
            if request.form['submit'] == "Learn More":
                return redirect('/details')
            elif registration.validate_on_submit() and request.form['submit'] == "Sign Up":
                return redirect('/order')
        return render_template("register.html",
             title = 'Register',
             form = registration)

    @app.route('/contact_confirmation')
    def contact_confirmation():
        return render_template("contact_confirmation.html")

    @app.route('/payment')
    def payment():
        return render_template("payment.html")

    @app.route('/paypal')
    def paypal():
        return render_template("paypal.html")

    @app.route('/creditcard', methods = ['GET', 'POST'])
    def creditcard():
        form = Payment()
        if form.validate_on_submit():
            flash('Thank you for your payment. Redirecting to confirmation page.')
            return redirect('/payment_confirmation')
        return render_template("creditcard.html",
             title = 'Credit Card Form',
             form = form)
    @app.route('/order')
    def info():
        form = Register()
        return render_template("order.html")

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
