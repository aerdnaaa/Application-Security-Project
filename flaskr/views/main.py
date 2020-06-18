from flask import Blueprint, render_template, request
from flask_login import current_user
from flaskr.forms import ContactUs

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/")
@main_blueprint.route("/Home")
def home():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    return render_template("main/Home.html", user=user)


@main_blueprint.route("/About")
def About():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    return render_template("main/About.html", user=user)


@main_blueprint.route("/FAQ")
def FAQ():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    return render_template("main/FAQ.html", user=user)


@main_blueprint.route("/Emailus", methods=["GET", "POST"])
def emailus():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    contactUsForm = ContactUs(request.form)
    return render_template("main/Emailus.html", user=user, form=contactUsForm)
