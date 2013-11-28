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

class PaypalForm(Form):
	phone_regex = '[\d\.\-\+\() ]+'
	name = TextField('Name', validators = [Required("Please enter your name")])
	email = TextField('Email', validators = [Optional(), validators.email("Your email is not valid")])
	phone = TextField('Phone', validators = [Optional(), validators.Regexp(phone_regex, message="Your phone number is not valid")])
	address1 = TextField('Address 1', validators = [Required("Please enter your address")])
	address2 = TextField('Address 2', validators=[Optional()])
	city = TextField('City', validators = [Required("Please enter your city")])
	state = SelectField('State', choices = [("1", "State"), ("2", "Alabama"), ("3", "Alaska"), ("4", "Arizona"),
	("5", "Arkansas"), ("6", "California"), ("7", "Colorado"), ("8", "Connecticut"), ("9", "Delaware"), ("10", "Florida"), ("11", "Georgia"), ("12", "Hawaii"), ("13", "Idaho"), ("14", "Illinois"),
	("15", "Indiana"), ("16", "Iowa"), ("17", "Kansas"), ("18", "Kentucky"), ("19", "Louisiana"), ("20", "Maine"), ("21", "Maryland"), ("22", "Massachusetts"), ("23", "Michigan"), ("24", "Minnesota"),
	("25", "Mississippi"), ("26", "Missouri"), ("27", "Montana"), ("28", "Nebraska"), ("29", "Nevada"), ("30", "New Hampshire"), ("31", "New Jersey"), ("32", "New Mexico"), ("33", "New York"), 
	("34", "North Carolina"), ("35", "North Dakota"), ("36", "Ohio"), ("37", "Oklahoma"), ("38", "Oregon"), ("39", "Pennsylvania"), ("40", "Rhode Island"), ("41", "South Carolina"),("42", "South Dakota"),
	("43", "Tennessee"), ("44", "Texas"), ("45", "Utah"), ("46", "Vermont"), ("47", "Virginia"), ("48", "Washington"), ("49", "West Virginia"), ("50", "Wisconsin"), ("51", "Wyoming")],
	validators = [Required("Please choose your state")])
	zipcode = TextField('Zip Code', validators = [Required("Please enter your zip code")])
	country = TextField('Country', validators = [Required("Please choose your country")])
	submit = SubmitField()

class CreditCardForm(Form):
	phone_regex = '[\d\.\-\+\() ]+'
	name = TextField('Name', validators = [Required("Please enter your name")])
	email = TextField('Email', validators = [Optional(), validators.email("Your email is not valid")])
	phone = TextField('Phone', validators = [Optional(), validators.Regexp(phone_regex, message="Your phone number is not valid")])
	address1 = TextField('Address 1', validators = [Required("Please enter your address")])
	address2 = TextField('Address 2', validators=[Optional()])
	city = TextField('City', validators = [Required("Please enter your city")])
	state = SelectField('State', choices = [("1", "State"), ("2", "Alabama"), ("3", "Alaska"), ("4", "Arizona"),
	("5", "Arkansas"), ("6", "California"), ("7", "Colorado"), ("8", "Connecticut"), ("9", "Delaware"), ("10", "Florida"), ("11", "Georgia"), ("12", "Hawaii"), ("13", "Idaho"), ("14", "Illinois"),
	("15", "Indiana"), ("16", "Iowa"), ("17", "Kansas"), ("18", "Kentucky"), ("19", "Louisiana"), ("20", "Maine"), ("21", "Maryland"), ("22", "Massachusetts"), ("23", "Michigan"), ("24", "Minnesota"),
	("25", "Mississippi"), ("26", "Missouri"), ("27", "Montana"), ("28", "Nebraska"), ("29", "Nevada"), ("30", "New Hampshire"), ("31", "New Jersey"), ("32", "New Mexico"), ("33", "New York"), 
	("34", "North Carolina"), ("35", "North Dakota"), ("36", "Ohio"), ("37", "Oklahoma"), ("38", "Oregon"), ("39", "Pennsylvania"), ("40", "Rhode Island"), ("41", "South Carolina"),("42", "South Dakota"),
	("43", "Tennessee"), ("44", "Texas"), ("45", "Utah"), ("46", "Vermont"), ("47", "Virginia"), ("48", "Washington"), ("49", "West Virginia"), ("50", "Wisconsin"), ("51", "Wyoming")],
	validators = [Required("Please choose your state")])
	zipcode = TextField('Zip Code', validators = [Required("Please enter your zip code")])
	country = TextField('Country', validators = [Required("Please choose your country")])
	submit = SubmitField()

class OrderForm(Form):
	jenkins = BooleanField('Jenkins', [validators.Optional()])
	selenium = BooleanField('Selenium', [validators.Optional()])
	fitnesse = BooleanField('FitNesse', [validators.Optional()])
	bugzilla = BooleanField('Bugzilla', [validators.Optional()])
	submit = SubmitField()
