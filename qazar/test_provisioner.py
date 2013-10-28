import os
from provisioner import Provisioner
from flask.ext.testing import TestCase

class TestProvisioner(TestCase):
    def test_setup(self):
        self.p = Provisioner()
    def test_init(self):
        self.assertIn("provision.log", os.listdir(os.path.dirname(os.path.realpath(__file__))))
    def test_provision(self):
        SQLALCHEMY_DATABASE_URI = "sqlite:///qazar.db"

    
