from flask import Blueprint, render_template

admin_blueprint = Blueprint('admin', __name__)


# ============================================= Admin Dashboard =============================================#
@admin_blueprint.route("/Admin")
def admin():
    return render_template("admin/Admin.html")
