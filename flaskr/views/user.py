from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from flaskr.forms import Register, SignIn, Forget, Recover
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
        if c.execute("SELECT username FROM users WHERE username='{}' ".format(register.username.data)).fetchone() == None:
            # Weak code (Not validating user input)
            c.execute("INSERT INTO users VALUES ('{}', '{}', '{}', '{}', '{}')".format(register.username.data, register.email.data, register.password.data, register.question.data, register.answer.data))
            conn.commit()
            conn.close()
            return redirect(url_for('user.signin'))
        else:
            # Weak code (Allows attacker to try repeatedly to find legitimate username)
            flash('Username exists! Please try again')
    return render_template("user/Register.html", user=user, form=register)


@user_blueprint.route("/Signin", methods=["GET", "POST"])
def signin():
    try:
        current_user.get_username()
        user = current_user
    except:
        user = None
    
    signin = SignIn(request.form)
    if request.method == "POST" and signin.validate():
        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        # Weak code (Not validating user input)
        # POSSIBLE ATTACKS
        # ' or 1=1-- (login to admin account)
        # user'-- (login to any account)
        # ' or rowid=1-- (login to any account)
        # ZAP' OR '1'='1' --
        c.execute("SELECT rowid, * FROM users WHERE username='{}' AND password='{}' ".format(signin.username.data, signin.password.data))
        conn.commit()
        user = c.fetchone()

        # Weak Code (disclosing too much information)
        if user == None:
            if c.execute("SELECT username FROM users WHERE username='{}'".format(signin.username.data)).fetchone() != None:
                flash("Incorrect password")
            else:
                flash("Incorrect username")

        elif user[1] == "Admin":
            userObj = User(user[0], user[1], user[2], user[3], user[4], user[5])
            print(user)
            login_user(userObj)
            return redirect(url_for('admin.admin'))

        else:
            userObj = User(user[0], user[1], user[2], user[3], user[4], user[5])
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

@user_blueprint.route('/forget', methods=["GET", "POST"])
def forget():
    forgetForm = Forget(request.form)
    if request.method == "POST" and forgetForm.validate():
        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        if c.execute("SELECT username FROM users WHERE username='{}' ".format(forgetForm.username.data)).fetchone() == None:
            flash("Username does not exist!")
        else:
            return redirect(url_for('user.recover', username=forgetForm.username.data))

    return render_template("user/Forget.html", form=forgetForm)

@user_blueprint.route('/recover/<username>', methods=["GET", "POST"])
def recover(username):
    conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM users WHERE username='{}' ".format(username))
    user = c.fetchone()
    userObj = User(user[0], user[1], user[2],user[3], user[4], user[5])

    recoverForm = Recover(request.form)
    if request.method == "POST" and recoverForm.validate():
        if recoverForm.answer.data.lower() == userObj.get_answer():
            c.execute("UPDATE users SET password='{}' WHERE username='{}' ".format(recoverForm.password.data, username))
            conn.commit()
            conn.close()
            return redirect(url_for('user.signin'))
        else:
            flash("Incorrect answer!")

    return render_template('user/Recover.html', user=userObj, form=recoverForm)


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
