from flask import Blueprint, render_template

admin_blueprint = Blueprint('admin', __name__)


# ============================================= Admin Dashboard =============================================#
@admin_blueprint.route("/Admin")
def admin():
    return render_template("admin/Admin.html", title="Dashboard")


@admin_blueprint.route("/Admin/add_product")
def add_product():
    category_list = ['barbell', 'bench', 'racks', 'plates']
    return render_template("admin/Add_Product.html", title="Add Product", category_list=category_list)


@admin_blueprint.route("/Admin/show_product")
def show_product():
    return render_template("admin/Show_Product.html", title="Products")