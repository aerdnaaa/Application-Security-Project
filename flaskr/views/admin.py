from flask import Blueprint, render_template
import sqlite3, os
from flaskr import file_directory

admin_blueprint = Blueprint('admin', __name__)


# ============================================= Admin Dashboard =============================================#
@admin_blueprint.route("/Admin")
def admin():
    return render_template("admin/Admin.html", title="Dashboard")


@admin_blueprint.route("/Admin/add_product")
def add_product():
    category_list = ['barbell', 'bench', 'racks', 'plates']
    return render_template("admin/Products/Add_Product.html", title="Add Product", category_list=category_list)


@admin_blueprint.route("/Admin/show_product")
def show_product():
    return render_template("admin/Products/Show_Product.html", title="Products")


@admin_blueprint.route("/Admin/show_voucher")
def show_voucher():
    return render_template("admin/Vouchers/Show_Voucher.html", title="Vouchers")


@admin_blueprint.route("/Admin/add_voucher")
def add_voucher():
    return render_template("admin/Vouchers/Add_Voucher.html", title="Add Voucher")


@admin_blueprint.route("/manage_user")
def manage_user():
    conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM users")
    users = c.fetchall()
    conn.close()
    return render_template("admin/Manage_Users/manage_user.html", title="users",users=users)


@admin_blueprint.route("/logs")
def logs():
    return render_template("admin/Logging/log.html", title="Logs")
