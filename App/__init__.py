from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


def get_todo():
    from App.api.todoSimple import TodoSimple
    return TodoSimple


api.add_resource(get_todo(), '/api')

from App.web import routes