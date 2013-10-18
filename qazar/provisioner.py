import logging
import subprocess

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
        subprocess.call(["alembic", "upgrade", "head"]) #create provisions table
    def provision(self, env):
        """
        """
        charms = env["charms"]
        for charm in charms:
            print self.name_to_script[charm["name"]]
        logging.info("determing provisioning script...")
        logging.info("creating database entry with requested status...")
        #subprocess.call(["alembic", "upgrade", "head"])
        logging.info("running provisioning script...")


