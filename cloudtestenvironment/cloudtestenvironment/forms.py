from flask.ext.wtf import Form, validators
from wtforms import TextField, BooleanField, SelectField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import Required, Optional, Length, Regexp


class RegistrationForm(Form):
	phone_regex = '[\d\.\-\+\() ]+'
	name = TextField('Name', validators = [Required("Please enter your name")])
	email = TextField('Email', validators = [Required("Please enter your email address"), validators.email("Your email address is not valid")])
	phone = TextField('Phone', validators = [Optional(), validators.Regexp(phone_regex, message="Your phone number is not valid")])
	company = TextField('Company')
	tell_me_more = SubmitField()
	sign_up = SubmitField()
	pagename = HiddenField()
	
class ContactForm(Form):
	phone_regex = '[\d\.\-\+\() ]+'
	name = TextField('Name', validators = [Required("Please enter your name")])
	email = TextField('Email', validators = [Required("Please enter your email address"), validators.email("Your email is not valid")])
	phone = TextField('Phone', validators = [Optional(), validators.Regexp(phone_regex, message="Your phone number is not valid")])
	message = TextAreaField('Message')
	send = SubmitField()

class PurchaseForm(Form):
	phone_regex = '[\d\.\-\+\() ]+'
	name = TextField('Name', validators = [Required("Please enter your name")])
	email = TextField('Email', validators = [Optional(), validators.email("Your email is not valid")])
	phone = TextField('Phone', validators = [Optional(), validators.Regexp(phone_regex, message="Your phone number is not valid")])
	address1 = TextField('Address 1', validators = [Required("Please enter your address")])
	address2 = TextField('Address 2', validators=[Optional()])
	city = TextField('City', validators = [Required("Please enter your city")])
	state = SelectField('State', validators = [Required("Please choose your state")])
	zipcode = TextField('Zip Code', validators = [Required("Please enter your zip code")])
	country = SelectField('Country', validators = [Required("Please choose your country")])
	submit = SubmitField()

class OrderForm(Form):
	jenkins = BooleanField('Jenkins', [validators.Optional()])
	selenium = BooleanField('Selenium', [validators.Optional()])
	fitnesse = BooleanField('FitNesse', [validators.Optional()])
	bugzilla = BooleanField('Bugzilla', [validators.Optional()])
	submit = SubmitField()
