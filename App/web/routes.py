from flask import render_template, url_for, request, redirect, flash
from App.web.Forms import Register, ContactUs, SignIn, SearchForm
from App import app, file_directory
import sqlite3, os
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from App.web.User import User

app.config['SECRET_KEY'] = 'ThisIsSupposedToBeSecret'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect(os.path.join(file_directory,"storage.db"))
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
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    register = Register(request.form)
    if request.method == "POST" and register.validate():
        conn = sqlite3.connect(os.path.join(file_directory,"storage.db"))
        c = conn.cursor()
        # Weak code (Not validating user input)
        c.execute("INSERT INTO users VALUES ('{}', '{}', '{}')".format(register.username.data, register.email.data, register.password.data))
        conn.commit()
        conn.close()
        return redirect(url_for('signin'))
    return render_template("Register.html", user=user, form=register)

@app.route("/Signin", methods=["GET", "POST"])
def signin():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    print(current_user)
    signin = SignIn(request.form)
    if request.method == "POST" and signin.validate():
        conn = sqlite3.connect(os.path.join(file_directory,"storage.db"))
        c = conn.cursor()
        # Weak code (Not validating user input)
        # POSSIBLE ATTACKS
        # ' or 1=1-- (login to admin account)
        # user'-- (login to any account)
        # ' or rowid=1-- (login to any account)
        c.execute("SELECT rowid, * FROM users WHERE username='{}' AND password='{}' ".format(signin.username.data, signin.password.data))
        conn.commit()
        user = c.fetchone()

        # Weak Code (disclosing too much information)
        if user == None:
            if c.execute("SELECT * FROM users WHERE username='{}'".format(signin.username.data)).fetchone() != None:
                flash("Incorrect password")
            else:
                flash("Incorrect username")

        elif user[1] == "Admin":
            userObj = User(user[0], user[1], user[2], user[3])
            print(user)
            login_user(userObj)
            return redirect(url_for('admin'))

        else:
            userObj = User(user[0], user[1], user[2], user[3])
            print(user)
            login_user(userObj)
            return redirect(url_for('home'))
        conn.close()
    return render_template("SignIn.html", user=user, form=signin)

@app.route('/logout')
# @login_required
def logout():
    logout_user()
    print('User logged out')
    return redirect(url_for('home'))
#===============================================================================================================#

@app.route("/")
@app.route("/Home")
def home():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    return render_template("Home.html", user=user)

@app.route("/ShoppingCart", methods=["GET", "POST"])
def ShoppingCart():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    return render_template("ShoppingCart.html", user=user)


@app.route("/Products", methods=['POST', 'GET'])
def Products():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    return render_template("Products.html", user=user)

@app.route("/About")
def About():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    return render_template("About.html", user=user)

@app.route("/FAQ")
def FAQ():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    return render_template("FAQ.html", user=user)

@app.route("/Emailus", methods =["GET", "POST"])
def emailus():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    contactUsForm = ContactUs(request.form)
    return render_template("Emailus.html", user=user, form=contactUsForm)

#============================================= Profile Page =============================================#
@app.route("/Profile", methods=["GET", "POST"])
@login_required
def Profile():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None

    return render_template("Profile.html", user=user)
#============================================= Admin Dashboard =============================================#
#Get key to sort products
def bySold_key(obj):
    return obj.get_sold()

@app.route("/Admin")
def admin():
    return render_template("Admin.html")




