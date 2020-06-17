from flask import render_template, url_for, request, redirect, flash
from App.web.Forms import Register, ContactUs, SignIn, SearchForm
from App import app
import sqlite3
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
import uuid

app.config['SECRET_KEY'] = 'ThisIsSupposedToBeSecret'

login_manager = LoginManager()
login_manager.init_app(app)

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
@app.route("/Register", methods=["GET","POST"])
def register():
    register = Register(request.form)
    if request.method == "POST" and register.validate():
        conn = sqlite3.connect("storage.db")
        c = conn.cursor()
        # Weak Code (not validating user input)
        c.execute("INSERT INTO users VALUES ('{}', '{}', '{}')".format(register.username.data, register.email.data, register.password.data))
        conn.commit()
        conn.close()
    return render_template("Register.html", form=register)

# Temporary
class User(UserMixin):
    def __init__(self, username, email, password):
        self.id = 123
        self.__username = username
        self.__email = email
        self.__password = password

    def get_username(self):
        return self.__username
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password


    def set_email(self, email):
        self.__email = email
    def set_password(self, password):
        self.__password = password

@login_manager.user_loader
def load_user(user_id):
    return 

@app.route("/SignIn", methods=["GET","POST"])
def signin():
    signin = SignIn(request.form)
    if request.method == "POST" and signin.validate():
        conn = sqlite3.connect("storage.db")
        c = conn.cursor()

        # Weak Code (not validating user input)
        c.execute("SELECT * FROM users WHERE username='{}' AND password='{}' ".format(signin.username.data, signin.password.data))
        conn.commit()
        user = c.fetchone()
        conn.close()

        # Get user obj and login user
        userObj = User(user[0], user[1], user[2])
        login_user(userObj)
        return redirect(url_for('Profile'))
    return render_template("SignIn.html", form=signin)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "User logout"

@app.route('/test')
@login_required
def test():
    return 'Current user is ' + current_user.get_username()

