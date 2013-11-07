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

	def provision(self, env=None):
		"""
		"""
		logging.info("determing provisioning script...")

		logging.info("creating database entry with requested status...")
		provision_requests = self.db['provision_requests']
		provision_request = {
			'environment': env,
			'status_information': {
				'status': 'requested',
				'requested_at': ""
				'requested_from': ip_address,
				'requested_by': "",
				'last_changed': ""
			}
		}
		provision_request_id = provision_requests.insert(provision_request)
		logging.info(self.db.collection_names())

		logging.info("running provisioning script...")
		for charm in env['description']:
			call(["juju", "deploy", charm])
			call(["juju", "expose", charm])


