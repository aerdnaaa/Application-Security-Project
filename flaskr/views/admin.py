from flask import Blueprint, render_template

admin_blueprint = Blueprint('admin', __name__)


# ============================================= Admin Dashboard =============================================#
# Get key to sort products
def bySold_key(obj):
    return obj.get_sold()


@admin_blueprint.route("/Admin")
def admin():
    return render_template("admin/Admin.html")
