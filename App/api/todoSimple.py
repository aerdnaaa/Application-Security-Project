from flask import request
from flask_restful import Resource
import sqlite3, os
from App import file_directory

todos = {}

class Users(Resource):
    def get(self):
        conn = sqlite3.connect(os.path.join(file_directory,"storage.db"))
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        conn.commit()
        user = c.fetchall()
        conn.close()
        print(user)
