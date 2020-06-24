from flask import Blueprint, render_template, request, redirect, url_for, flash, session, make_response
from flaskr.forms import Register, SignIn, Forget, Recover, PaymentOptions
from flaskr import file_directory
from flaskr.models.User import User
import sqlite3, os

user_blueprint = Blueprint('user', __name__)


# ============================================= Sign in/ Register ===============================================#
@user_blueprint.route("/Register", methods=["GET", "POST"])
def register():
    if 'username' in session:
        return redirect(url_for('main.home'))
    else:
        user = None

    register = Register(request.form)
    if request.method == "POST" and register.validate():
        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        if c.execute(
            "SELECT username FROM users WHERE username='{}' ".format(register.username.data)).fetchone() == None:
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
    if 'username' in session:
        return redirect(url_for('main.home'))
    else:
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
        c.execute("SELECT * FROM users WHERE username='{}' AND password='{}' ".format(signin.username.data, signin.password.data))
        conn.commit()
        user = c.fetchone()

        # Weak Code (disclosing too much information)
        if user == None:
            if c.execute(
                    "SELECT username FROM users WHERE username='{}'".format(signin.username.data)).fetchone() != None:
                flash("Incorrect password")
            else:
                flash("Incorrect username")

        elif user[0] == "Admin":
            # Weak code: Store confidential info in session
            session['username'] = user[0]
            session['email'] = user[1]
            session['password'] = user[2]
            session['question'] = user[3]
            session['answer'] = user[4]
            return redirect(url_for('admin.admin'))

        else:
            # Weak code: Store confidential info in session
            session['username'] = user[0]
            session['email'] = user[1]
            session['password'] = user[2]
            session['question'] = user[3]
            session['answer'] = user[4]
            return redirect(url_for('main.home'))
        conn.close()
    return render_template("user/SignIn.html", user=user, form=signin)


@user_blueprint.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    session.pop('password', None)
    session.pop('question', None)
    session.pop('answer', None)
    session.pop('cart', None)
    return redirect(url_for('main.home'))


@user_blueprint.route('/forget', methods=["GET", "POST"])
def forget():
    if 'username' in session:
        return redirect(url_for('main.home'))
    else:
        user = None

    forgetForm = Forget(request.form)
    if request.method == "POST" and forgetForm.validate():
        conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
        c = conn.cursor()
        if c.execute(
                "SELECT username FROM users WHERE username='{}' ".format(forgetForm.username.data)).fetchone() == None:
            flash("Username does not exist!")
        else:
            return redirect(url_for('user.recover', username=forgetForm.username.data))

    return render_template("user/Forget.html", form=forgetForm, user=user)


@user_blueprint.route('/recover/<username>', methods=["GET", "POST"])
def recover(username):
    if 'username' in session:
        return redirect(url_for('main.home'))

    conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username='{}' ".format(username))
    user = c.fetchone()
    userObj = User(user[0], user[1], user[2], user[3], user[4])

    recoverForm = Recover(request.form)
    if request.method == "POST" and recoverForm.validate():
        if recoverForm.answer.data.lower() == userObj.get_answer():
            c.execute("UPDATE users SET password='{}' WHERE username='{}' ".format(recoverForm.password.data, username))
            conn.commit()
            conn.close()
            # return redirect(url_for('user.signin'))
            flash("Password has been changed!", "success")
        else:
            flash("Incorrect answer!", "error")

    return render_template('user/Recover.html', user=None, userObj=userObj, form=recoverForm)


# ============================================= User Page =============================================#
@user_blueprint.route("/Profile", methods=["GET", "POST"])
def Profile():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        return redirect(url_for('user.signin'))

    return render_template("user/Profile.html", user=user)

@user_blueprint.route("/PaymentInfo", methods=["GET", "POST"])
def PaymentInfo():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        return redirect(url_for('user.signin'))

    payment = PaymentOptions(request.form)

    return render_template("user/Payment.html", user=user, form=payment)
