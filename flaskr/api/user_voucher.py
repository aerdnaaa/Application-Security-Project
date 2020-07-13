from flask import request, jsonify, redirect, url_for
from flask_restful import Resource
import sqlite3, os
from flaskr import file_directory


class UserVoucher(Resource):
    def get(self, user_id):
        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        # TODO change user_vouchers to vouchers table
        c.execute("SELECT * FROM vouchers WHERE user_id = {}".format(user_id))
        conn.commit()
        vouchers = [dict(row) for row in c.fetchall()]
        conn.close()

        return jsonify(data=vouchers)

    def post(self, user_id):
        # TODO validate if voucher_code and voucher_title exists in voucher table
        request_json_data = request.get_json(force=True)
        voucher_title = request_json_data["title"]
        voucher_code = request_json_data["code"]
        voucher_image = ""
        voucher_description = request_json_data["description"]
        voucher_amount = request_json_data["amount"]
        voucher_status = "unused"
        used_date = ""

        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()

        # Validate if voucher title is in database
        c.execute(f"SELECT * FROM vouchers WHERE title='{voucher_title}'")
        if c.fetchone():
            response = jsonify(data="Voucher Title is used.")
            response.status_code = 400
            return response

        # Validate if voucher code is in database
        c.execute(f"SELECT * FROM vouchers WHERE code='{voucher_code}'")
        if c.fetchone():
            response = jsonify(data="Voucher Code is used.")
            response.status_code = 400
            return response

        c.execute("INSERT INTO vouchers VALUES ('{}', '{}', '{}', {}, '{}', '{}', {})".format(voucher_title, voucher_code, voucher_description, voucher_image, voucher_amount, voucher_status, used_date, user_id))
        conn.commit()
        conn.close()

        return jsonify(data="Voucher created with user id of {}".format(user_id))

    def put(self, user_id):
        # TODO ensure this is working
        import datetime
        request_json_data = request.get_json(force=True)
        code = request_json_data["code"]
        used_date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        c.execute("SELECT * FROM vouchers WHERE code = '{}' AND status = 'unused'".format(code))

        if c.fetchone():
            c.execute("UPDATE vouchers SET status = 'used', used_date = '{}' WHERE code = '{}'".format(used_date, code))
            conn.commit()
            conn.close()

            return jsonify(data=f"Voucher with the code {code} from user id {user_id} has been used.")

        else:
            conn.commit()
            conn.close()

            return jsonify(data=f"Voucher with the code {code} from user id {user_id} has already been used.")


