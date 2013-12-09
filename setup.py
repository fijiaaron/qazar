from setuptools import setup

setup(
	name="qazar",
	version="0.1"
	url="http://cloudtestenvironment.com",
	author="One Shore"
	author_email="aarone@one-shore.com"
	install_requires=[
		Flask==0.10.1,
		Flask-SQLAlchemy==0.16,
		Flask-WTF==0.8.4,
		Jinja2==2.7.1,
		Mako==0.9.0,
		MarkupSafe==0.18,
		SQLAlchemy==0.8.2,
		WTForms==1.0.5,
		Werkzeug==0.9.4,
		pymongo==2.6.3,
		requests==2.0.1,
		twill==0.9,
		wsgiref==0.1.2,
	],
	test_suite=""
	entry_points={
		"distutils.commands": [
			"runserver = ",
		],
	},
)
