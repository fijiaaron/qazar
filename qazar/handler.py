from flask import Flask, request
from provisioner import Provisioner

app = Flask(__name__)

@app.route('/provision', methods = ['POST'])
def provision():
	environment = {'description': request.args['description']}
	p = Provisioner()
	p.provision(environment)
