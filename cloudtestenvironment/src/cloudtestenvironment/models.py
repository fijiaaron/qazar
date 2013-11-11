from flask.ext.sqlalchemy import SQLAlchemy
from cloudtestenvironment import app

db = SQLAlchemy(app)

class Contact(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(40))
        email = db.Column(db.String(40))
        phone = db.Column(db.String(15))
        message = db.Column(db.String(500))

        def __init__(self, name, email, phone, message):
                self.name = name
                self.email = email
                self.phone = phone
                self.message = message

class Customer(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(40))
        email = db.Column(db.String(40))
        phone = db.Column(db.String(15))
        company = db.Column(db.String(40))
        registered = db.Column(db.Boolean)

        def __init__(self, name, email, phone, company, registered=False):
                self.name = name
                self.email = email
                self.phone = phone
                self.company = company
                self.registered = registered
