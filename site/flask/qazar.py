from flask import Flask
app = Flask(__name__);

@app.route('/')
def hello():
	content = "Qazar with Gunicorn and Flask!"
	return content


if __name__ == "__main__":
	app.run()