from flask import Flask
from flask_restful import Api
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_mail import Mail
import os, sqlite3

app = Flask(__name__)
api_app = Api(app)
jwt = JWTManager(app)
mail = Mail(app)
app.config.from_object('config')

file_directory = os.path.dirname(os.path.dirname(__file__))

from flaskr.api.users import Users
from flaskr.api.login import Login
from flaskr.api.retrieve_password import Retrieve_Password

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
