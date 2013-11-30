from database import db_session
from cloudtestenvironmentapp import CloudTestEnvironmentApp
from cloudtestenvironmentwebapp import CloudTestEnvironmentWebApp

app = CloudTestEnvironmentApp(db_session)
web_app = CloudTestEnvironmentWebApp(__name__, static_folder='static', static_url_path='')
web_app.config.from_object('config')
web_app.init_app()
