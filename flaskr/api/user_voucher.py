from flask import request, jsonify, redirect, url_for
from flask_restful import Resource
import sqlite3, os
from flaskr import file_directory


class UserVoucher(Resource):
    def get(self, user_id):
        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM user_vouchers WHERE user_id = {}".format(user_id))
        conn.commit()
        vouchers = [dict(row) for row in c.fetchall()]
        conn.close()

        return jsonify(data=vouchers)

    def post(self, user_id):
        request_json_data = request.get_json(force=True)
        name = request_json_data["name"]
        code = request_json_data["code"]
        description = request_json_data["description"]
        amount = request_json_data["amount"]
        status = "unused"
        used_date = ""

        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        c.execute("INSERT INTO user_vouchers VALUES ('{}', '{}', '{}', {}, '{}', '{}', {})".format(name, code, description, amount, status, used_date, user_id))
        conn.commit()
        conn.close()

        return jsonify(data="Voucher created with user id of {}".format(user_id))

    def put(self, user_id):
        import datetime
        request_json_data = request.get_json(force=True)
        code = request_json_data["code"]
        used_date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        c.execute("SELECT * FROM user_vouchers WHERE code = '{}' AND status = 'unused'".format(code))

        if c.fetchone():
            c.execute("UPDATE user_vouchers SET status = 'used', used_date = '{}' WHERE code = '{}'".format(used_date, code))
            conn.commit()
            conn.close()

            return jsonify(data=f"Voucher with the code {code} from user id {user_id} has been used.")

        else:
            conn.commit()
            conn.close()

            return jsonify(data=f"Voucher with the code {code} from user id {user_id} has already been used.")


