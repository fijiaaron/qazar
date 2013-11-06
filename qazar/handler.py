from flask import Flask, request

app = Flask(__name__)

@app.route('/provision', methods = ['POST'])
def provision():
	order = {"":request.args[""]}
