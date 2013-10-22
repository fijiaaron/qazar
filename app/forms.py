from flask.ext.wtf import Form, validators
from wtforms import TextField, BooleanField, SelectField, HiddenField
from wtforms.validators import Required, Length

class Register(Form):
    name= TextField('Name', validators= [Required("Please enter your name.")])
    email= TextField('Email', validators= [Required("Please enter your e-mail.")])
    phone= TextField('Phone')
    company= TextField('Company')
    hasErrors= TextField('hasErrors')

class Payment(Form):
 	ccnumber= TextField('Credit Card Number', validators= [Required()])
 	cvv= TextField('CVV', validators= [Required()])
 	expmonth= SelectField(u'Month', validators = [Length(min=15), Required()], description={'placeholder: Month'}, choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])
 	expyear = SelectField(u'Year', choices=[(1, '2013')])
 	name= TextField('Card Holder Name', validators = [Required()])
 	address1= TextField('Address1', validators = [Required()])
 	address2= TextField('Address2')
 	city= TextField('City', validators = [Required()])
 	state= TextField('State', validators = [Required()])
 	zipcode= TextField('Zip Code', validators = [Required()])