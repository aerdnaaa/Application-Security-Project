from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api_app = Api(app)



from App.api.todoSimple import TodoSimple
api_app.add_resource(TodoSimple, '/api')

from App.web import routes
