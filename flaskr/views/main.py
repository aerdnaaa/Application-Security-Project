from flask import Blueprint, render_template, request, session
from flaskr.models.User import User
from flaskr.forms import ContactUs

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/")
@main_blueprint.route("/Home")
def home():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None

    return render_template("main/Home.html", user=user)


@main_blueprint.route("/About")
def About():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None

    return render_template("main/About.html", user=user)


@main_blueprint.route("/FAQ")
def FAQ():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None

    return render_template("main/FAQ.html", user=user)


@main_blueprint.route("/Emailus", methods=["GET", "POST"])
def emailus():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None
        
    contactUsForm = ContactUs(request.form)
    return render_template("main/Emailus.html", user=user, form=contactUsForm)
