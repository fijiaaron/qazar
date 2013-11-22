from cloudtestenvironment import app, db
from cloudtestenvironment.controllers import RegistrationController

from pprint import pprint as pp

#ready to start testing and implementing

def setup():
	print("")
	print("creating registration controller")
	registration = RegistrationController(app.config)
	registration.set_db(db)
	pp(registration)

registration = RegistrationController(None)
registration.set_db(db)

fixture = { 'registration' : registration }
def test_registration_has_db():
	assert registration.db