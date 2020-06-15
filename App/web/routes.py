from flask import render_template, url_for, request, redirect, flash
from App.web.Forms import Register, ContactUs, SignIn, SearchForm
from App import app


@app.route("/")
@app.route("/Home")
def home():
    return render_template("Home.html")

@app.route("/ShoppingCart", methods=["GET", "POST"])
def ShoppingCart():
    return render_template("ShoppingCart.html")


@app.route("/Products", methods=['POST', 'GET'])
def Products():
        return render_template("Products.html")

@app.route("/About")
def About():
    return render_template("About.html")

@app.route("/FAQ")
def FAQ():
    return render_template("FAQ.html")

@app.route("/Emailus", methods =["GET", "POST"])
def emailus():
    contactUsForm = ContactUs(request.form)
    return render_template("Emailus.html", form=contactUsForm)

#============================================= Profile Page =============================================#
@app.route("/Profile", methods=["GET", "POST"])
def Profile():
    return render_template("Profile.html")
#============================================= Admin Dashboard =============================================#
#Get key to sort products
def bySold_key(obj):
    return obj.get_sold()

@app.route("/Admin")
def admin():
    return render_template("Admin.html")
#===========================================================================================================#
@app.route("/Register", methods=["GET", "POST"])
def register():
    register = Register(request.form)
    return render_template("Register.html", form=register)

@app.route("/SignIn", methods=["GET", "POST"])
def signin():
    signin = SignIn(request.form)
    return render_template("SignIn.html", form=signin)

