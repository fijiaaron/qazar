from cloudtestenvironment.models import db
from flask import Flask
import unittest

class TestExample(unittest.TestCase):

	def user(self):
		self.app = Flask(__name__)
		db.init_app(self.app)
		with self.app.app_context():
			db.create_all()