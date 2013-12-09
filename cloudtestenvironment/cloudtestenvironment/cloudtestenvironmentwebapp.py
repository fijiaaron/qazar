from flask import Flask
from database import init_db

class CloudTestEnvironmentWebApp(Flask):
	"""
	"""
	def init_app(self):
		init_db()
		from cloudtestenvironment import routes
		
