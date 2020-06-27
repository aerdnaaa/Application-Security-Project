from flask import request, jsonify, redirect, url_for
from flask_restful import Resource
import sqlite3, os
from flaskr import file_directory


class Vouchers(Resource):
    def get(self):
        voucher_list = []
        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        c.execute(f"SELECT * FROM vouchers ")
        vouchers = c.fetchall()
        for voucher in vouchers:
            voucher_list.append(
                {"voucherName": voucher[0], "voucherImage": voucher[1], "voucherCode": voucher[2], "voucherDescription": voucher[3], "voucherAmount": voucher[4], "status": voucher[5]})
        return jsonify(data=voucher_list)

    def post(self):
        voucher_name = request.form.get('voucherNameInput')
        voucher_img = request.files.get('voucherImage')
        voucher_code = request.form.get('voucherCode')
        voucher_description = request.form.get('voucherDescription')
        voucher_ammount = request.form.get('voucherAmountInput')


        filename = voucher_img.filename
        filepath = 'products/' + filename
        voucher_img.save(os.path.join(file_directory, 'flaskr/static/img/vouchers', filename))

        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        c.execute(
            f"INSERT INTO vouchers VALUES ('{voucher_name}', '{filepath}', '{voucher_code}','{voucher_description}', '{voucher_ammount}','active')")
        conn.commit()

        if request.user_agent.string[:14] != "PostmanRuntime":
            return redirect(url_for('admin.show_vouchers'))

        return jsonify(data="Success")

    def put(self):
        request_json_data = request.get_json(force=True)

        voucher_name = request_json_data['voucher_name']
        voucher_status = request_json_data['voucher_status']

        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        c.execute(f"UPDATE vouchers SET status = '{voucher_status}' WHERE name = '{voucher_name}'")
        conn.commit()

        return jsonify(data="Success")
