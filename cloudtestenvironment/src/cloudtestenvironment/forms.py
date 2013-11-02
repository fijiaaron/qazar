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



class ContactForm(Form):
	phone_regex = '[\d\.\-\+\() ]+'
	name = TextField('Name', validators = [Required("Please enter your name")])
	email = TextField('Email', validators = [Required("Please enter your email address"), validators.email("Your email is not valid")])
	phone = TextField('Phone', validators = [Optional(), validators.Regexp(phone_regex, message="Your phone number is not valid")])
	message = TextAreaField('Message')
	send = SubmitField()