from cloudtestenvironment import app, db
from cloudtestenvironment.controllers import RegistrationController

from pprint import pprint as pp

registration = None
def setup():
	print("")
	print("creating registration controller")
	global registration
	registration = RegistrationController(app.config)
	registration.set_db(db)
	pp(registration)


def test_registration_has_db():
	assert registration.db

	