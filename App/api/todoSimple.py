from App import api
from flask import request
from flask_restful import Resource

todos = {}


class TodoSimple(Resource):
    def get(self):
        return "hi there"
