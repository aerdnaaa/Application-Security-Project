from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from flaskr.forms import Register, SignIn
from flaskr import file_directory
from flaskr.models.User import User
import sqlite3, os

user_blueprint = Blueprint('user', __name__)


# ============================================= Sign in/ Register ===============================================#
@user_blueprint.route("/Register", methods=["GET", "POST"])
def register():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    register = Register(request.form)
    if request.method == "POST" and register.validate():
        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        # Weak code (Not validating user input)
        c.execute("INSERT INTO users VALUES ('{}', '{}', '{}')".format(register.username.data, register.email.data,
                                                                       register.password.data))
        conn.commit()
        conn.close()
        return redirect(url_for('user_blueprint.signin'))
    return render_template("user/Register.html", user=user, form=register)


@user_blueprint.route("/Signin", methods=["GET", "POST"])
def signin():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    print(current_user)
    signin = SignIn(request.form)
    if request.method == "POST" and signin.validate():
        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        # Weak code (Not validating user input)
        # POSSIBLE ATTACKS
        # ' or 1=1-- (login to admin account)
        # user'-- (login to any account)
        # ' or rowid=1-- (login to any account)
        c.execute("SELECT rowid, * FROM users WHERE username='{}' AND password='{}' ".format(signin.username.data,
                                                                                             signin.password.data))
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
            return redirect(url_for('admin_blueprint.admin'))

        else:
            userObj = User(user[0], user[1], user[2], user[3])
            print(user)
            login_user(userObj)
            return redirect(url_for('main.home'))
        conn.close()
    return render_template("user/SignIn.html", user=user, form=signin)


@user_blueprint.route('/logout')
# @login_required
def logout():
    logout_user()
    print('User logged out')
    return redirect(url_for('main.home'))


# ===============================================================================================================#

# ============================================= Profile Page =============================================#
@user_blueprint.route("/Profile", methods=["GET", "POST"])
@login_required
def Profile():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None

    return render_template("user/Profile.html", user=user)
