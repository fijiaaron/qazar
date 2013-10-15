import os
import sqlite3
import logging

class Provisioner():
    """
    """
    def __init__(self, settings=None):
        """
        """
        self.name_to_script = {"selenium": "juju deploy selenium", 
                               "jenkins": "juju deploy jenkins"} # in place of provisioning for now
        logging.basicConfig(filename="provision.log", level=logging.DEBUG)
    def provision(self, env):
        """
        """
        charms = env["charms"]
        if not os.path.isfile("qazar.db"):
            connection = sqlite3.connect("qazar.db")
            cursor = connection.cursor()
            cursor.execute("""
                           CREATE TABLE provisions
                           (id int primary key autoincrement,
                           user_id int, ip_address varchar(15), status int)
                           """)
        else:
            connection = sqlite3.connect("qazar.db")
            cursor = connection.cursor()
        for charm in charms:
            print self.name_to_script[charm["name"]]
        #cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        #print(cursor.fetchall())
        connection.close()

