from flask import Flask
from cloudtestenvironment.models import db
from cloudtestenvironment.application_factory import CloudTestEnvironment

app = CloudTestEnvironment(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')
app.set_db(db)
app.db.init_app(app)
with app.test_request_context():
	app.db.create_all()
from cloudtestenvironment import routes
