from flask import Blueprint, render_template, session, request, redirect, url_for
from flaskr.models.User import User
from flaskr.forms import SearchForm

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

    return render_template("shopping/Search.html", user=user)