from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField
from wtforms.validators import Required

class Register(Form):
    name= TextField('Name', validators = [Required()])
    email= TextField('Email', validators = [Required()])
    phone= TextField('Phone')
    company= TextField('Company')

class Payment(Form):
 	ccnumber= TextField('Credit Card Number', validators= [Required()])
 	cvv= TextField('CVV', validators= [Required()])
 	expmonth= SelectField('Month', choices=[('January'),('February'),('March'),('April'),('May'),('June'),('July'),('August'),('September'),('November'),('December')])
