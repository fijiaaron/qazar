from flask import Flask, request
from provisioner import Provisioner

app = Flask(__name__)

@app.route('/provision', methods = ['POST'])
def provision():
	environment = {'description': request.args['description']}
	status_information = {
		'time': request.args['time'],
		'ip_address': request.args['ip_address'],
		'customer': request.args['customer']
	}
	p = Provisioner()
	p.provision(environment, status_information)
	return "POSTED"

app.run(host='127.0.0.1', port=5050, debug=True)
