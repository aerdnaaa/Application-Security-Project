from flask import Flask
from flask_restful import Api
import os

app = Flask(__name__)
api_app = Api(app)

file_directory = os.path.dirname(os.path.dirname(__file__))

from App.api.todoSimple import Users
api_app.add_resource(Users, '/api/user')

from App.web import routes
