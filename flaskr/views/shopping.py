from flask import Blueprint, render_template, session, request, redirect, url_for
from flaskr.models.User import User
from flaskr.forms import SearchForm
import sqlite3, os
from flaskr import file_directory

shopping_blueprint = Blueprint('shopping', __name__)


@shopping_blueprint.route("/ShoppingCart", methods=["GET", "POST"])
def ShoppingCart():
    if 'username' in session:
        user = User(session['username'], session['email'], session['password'], session['question'], session['answer'])
    else:
        user = None

    return render_template("shopping/ShoppingCart.html", user=user)


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
        # Pass prodduct into url directly (Weak code)
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
    ' UNION SELECT * FROM x-- (Error: No such table x)
    ' UNION SELECT '1' FROM sqlite_master-- (Error: SELECTs to the left and right of UNION do not have the same number of result columns)
    ' UNION SELECT '1', '2', '3', '4', '5', '6' FROM sqlite_master-- (Returns all products)
    ' UNION SELECT '1', sql, '3', '4', '5', '6' FROM sqlite_master-- (Returns all tables in schema)
    """

    # Search Form
    form = SearchForm(request.form)
    if request.method == "POST":
        # Pass prodduct into url directly (Weak code)
        return redirect(url_for('shopping.Search', product=form.Search.data))

    return render_template("shopping/Search.html", user=user, products=results, search=product, form=form)