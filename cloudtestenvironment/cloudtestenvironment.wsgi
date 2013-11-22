import os, sys

cloudtestenvironment = os.path.abspath(".")
sys.path.insert(0, cloudtestenvironment)

from cloudtestenvironment import app as application
