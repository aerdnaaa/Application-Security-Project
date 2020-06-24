from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
import os, sqlite3
import logging
import sentry_sdk


#sentry sdk for logging
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.flask import FlaskIntegration
# All of this is already happening by default!
sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)
sentry_sdk.init(
    dsn="https://6adb767a90f14dee90f656e1e355f0b1@o412137.ingest.sentry.io/5288433",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
api_app = Api(app)
jwt = JWTManager(app)
mail = Mail(app)
CORS(app)
app.config.from_object('config')

file_directory = os.path.dirname(os.path.dirname(__file__))

from flaskr.api.users import Users
from flaskr.api.login import Login
from flaskr.api.retrieve_password import Retrieve_Password
from flaskr.api.products import Products

api_app.add_resource(Products, '/api/products')
api_app.add_resource(Users, '/api/user')
api_app.add_resource(Login, '/api/login')
api_app.add_resource(Retrieve_Password, '/api/retrieve_password')

from flaskr.models.User import User

from flaskr.views.admin import admin_blueprint
from flaskr.views.main import main_blueprint
from flaskr.views.shopping import shopping_blueprint
from flaskr.views.user import user_blueprint

app.register_blueprint(admin_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(shopping_blueprint)
app.register_blueprint(user_blueprint)

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

@app.route('/issues')
def sentry_issues():
    return ("https://sentry.io/api/0/project/Indirect/Indirect/issues/")