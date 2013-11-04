import logging
import pymongo
from subprocess import call

class Provisioner():
	"""
	"""
	def __init__(self, settings=None):
		"""
		"""
		logging.basicConfig(filename='provision.log', filemode='w', level=logging.DEBUG)
		logging.info("configuring provisioning...")
		client = pymongo.MongoClient()
		self.db = client['qazar']

	def provision(self, ip_address, env=None):
		"""
		"""
		logging.info("determing provisioning script...")

		logging.info("creating database entry with requested status...")
		provision_requests = self.db['provision_requests']
		provision_request = {
							"user_id": 0,
							"ip_address": ip_address,
							"status": "requested"
							}
		provision_request_id = provision_requests.insert(provision_request)
		logging.info(self.db.collection_names())


		logging.info("running provisioning script...")



