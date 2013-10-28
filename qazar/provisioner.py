import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from db import ProvisionRequest, set_up

class Provisioner():
    """
    """
    def __init__(self, settings=None):
        """
        """
        self.name_to_script = {"selenium": "juju deploy selenium", 
                               "jenkins": "juju deploy jenkins"} # in place of provisioning for now
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
        #charms = env["charms"]
        #for charm in charms:
            #print self.name_to_script[charm["name"]]


