from flask import request, jsonify
from flask_restful import Resource
import sqlite3, os
from flaskr import file_directory


class Products(Resource):
    def get(self):
        product_list = []
        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        c.execute(f"SELECT * FROM products ")
        products = c.fetchall()
        for product in products:
            product_list.append(
                {"productName": product[0], "productSellingPrice": product[1], "productCostPrice": product[2], "status":product[3]})
        return jsonify(data=product_list)

    def post(self):
        request_json_data = request.get_json(force=True)

        product_name = request_json_data['product_name']
        product_selling_price = request_json_data['product_selling_price']
        product_cost_price = request_json_data['product_cost_price']

        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        c.execute(f"INSERT INTO products VALUES ('{product_name}', '{product_selling_price}', '{product_cost_price}', 'active')")
        conn.commit()

        return jsonify(data="Success")

    def put(self):
        request_json_data = request.get_json(force=True)

        product_name = request_json_data['product_name']
        product_status = request_json_data['product_status']

        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        c.execute(f"UPDATE products SET product_status = '{product_status}' WHERE product_name = '{product_name}'")
        conn.commit()

        return jsonify(data="Success")
