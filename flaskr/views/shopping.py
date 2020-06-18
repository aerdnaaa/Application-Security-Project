from flask import Blueprint, render_template
from flask_login import current_user

shopping_blueprint = Blueprint('shopping', __name__)


@shopping_blueprint.route("/ShoppingCart", methods=["GET", "POST"])
def ShoppingCart():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    return render_template("shopping/ShoppingCart.html", user=user)


@shopping_blueprint.route("/Products", methods=['POST', 'GET'])
def Products():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    return render_template("shopping/Products.html", user=user)
