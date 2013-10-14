from flask import render_template
from app import app

class Helper():
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

    @app.route('/register')
    def register():
        return render_template("register.html")

    @app.route('/contact_confirmation')
    def contact_confirmation():
        return render_template("contact_confirmation.html")

    @app.route('/payment')
    def payment_confirmation():
        return render_template("payment.html")

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
