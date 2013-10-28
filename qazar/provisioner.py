import logging
from sqlalchemy.orm import sessionmaker
from db import ProvisionRequest, set_up

class Provisioner():
    """
    """
    def __init__(self, settings=None):
        """
        """
        logging.basicConfig(filename='provision.log', filemode='w', level=logging.DEBUG)
        logging.info("configuring provisioning...")
        self.engine = set_up()

    def provision(self, ip_address):
        """
        """
        logging.info("determing provisioning script...")
        
        logging.info("creating database entry with requested status...")
        Session = sessionmaker(bind=self.engine)
        session = Session()
        provision_request = ProvisionRequest(12345, ip_address, 0)
        session.add(provision_request)
        session.commit()

        logging.info("running provisioning script...")


