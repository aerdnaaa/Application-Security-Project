from flask import Flask
from flask_restful import Api
from flask_login import LoginManager
import os, sqlite3

app = Flask(__name__)
app.config.from_object('config')
api_app = Api(app)
login_manager = LoginManager(app)

file_directory = os.path.dirname(os.path.dirname(__file__))

from flaskr.api.users import Users
api_app.add_resource(Users, '/api/user')

from flaskr.models.User import User
@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect(os.path.join(file_directory,"storage.db"))
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM users WHERE rowid={} ".format(user_id))
    conn.commit()
    user = c.fetchone()
    conn.close()
    userObj = User(user[0], user[1], user[2], user[3])
    return userObj

from flaskr.views.admin import admin_blueprint
from flaskr.views.main import main_blueprint
from flaskr.views.shopping import shopping_blueprint
from flaskr.views.user import user_blueprint

app.register_blueprint(admin_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(shopping_blueprint)
app.register_blueprint(user_blueprint)
