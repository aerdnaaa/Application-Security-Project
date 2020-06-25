from flask import Blueprint, render_template, request, session
from flaskr.models.User import User
from flaskr.forms import ContactUs
import sqlite3, os
from flaskr import file_directory

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/")
@main_blueprint.route("/Home")
def home():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None
    
    conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM products")
    products = c.fetchall()
    conn.close()

    return render_template("main/Home.html", user=user, products=products)


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

@main_blueprint.route("/Reviews/<productid>", methods=["GET", "POST"])
def reviews(productid):
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None

    conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
    c = conn.cursor()
    c.execute("SELECT rowid,* FROM products WHERE rowid={}".format(productid))
    product = c.fetchone()

    c.execute("SELECT * FROM reviews")
    reviews=c.fetchall()
    conn.close()


    return render_template("main/Reviews.html", user=user, product=product, reviews=reviews)
