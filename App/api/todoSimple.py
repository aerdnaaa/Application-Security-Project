from App import api
from flask import request
from flask_restful import Resource

todos = {}


class TodoSimple(Resource):
    def get(self):
        return todos

    def put(self):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
