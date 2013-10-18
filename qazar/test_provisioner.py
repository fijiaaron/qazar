import os
import unittest
from provisioner import Provisioner
from sqlalchemy import create_engine
class TestProvisioner(unittest.TestCase):
    def test_setup(self):
        self.p = Provisioner()
    def test_init(self):
        self.assertIn("provision.log", os.listdir(os.path.dirname(os.path.realpath(__file__))))
    def test_provision(self):
        self.assertTrue(create_engine("sqlite:///qazar.db"))

    
