from flask import render_template, url_for, request, redirect, flash
from App.web.Forms import Register, ContactUs, SignIn, SearchForm
from App import app
import sqlite3
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from App.web.User import User

app.config['SECRET_KEY'] = 'ThisIsSupposedToBeSecret'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect("storage.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM users WHERE rowid={} ".format(user_id))
    conn.commit()
    user = c.fetchone()
    conn.close()
    userObj = User(user[0], user[1], user[2], user[3])
    return userObj

#============================================= Sign in/ Register ===============================================#
@app.route("/Register", methods=["GET", "POST"])
def register():
    register = Register(request.form)
    if request.method == "POST":
        conn = sqlite3.connect("storage.db")
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES ('{}', '{}', '{}')".format(register.username.data, register.email.data, register.password.data))
        conn.commit()
        conn.close()
    return render_template("Register.html", form=register)

@app.route("/Signin", methods=["GET", "POST"])
def signin():
    signin = SignIn(request.form)
    if request.method == "POST":
        conn = sqlite3.connect("storage.db")
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM users WHERE username='{}' AND password='{}' ".format(signin.username.data, signin.password.data))
        conn.commit()
        user = c.fetchone()
        conn.close()
        userObj = User(user[0], user[1], user[2], user[3])
        print(user)
        login_user(userObj)
        return redirect(url_for('Profile'))
    return render_template("SignIn.html", form=signin)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    print('User logged out')
    return redirect(url_for('home'))
#===============================================================================================================#

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
@login_required
def Profile():
    currentUser = current_user
    return render_template("Profile.html", currentUser=currentUser)
#============================================= Admin Dashboard =============================================#
#Get key to sort products
def bySold_key(obj):
    return obj.get_sold()

@app.route("/Admin")
def admin():
    return render_template("Admin.html")




