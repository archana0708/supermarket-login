from flask import Flask, jsonify, render_template, request, flash
from sql_connection import get_sql_connection
from products_dao import get_all_products

connection = get_sql_connection()

app = Flask(__name__)


@app.route('/getProducts', methods=['POST', 'GET'])
def getProducts():
    products = get_all_products(connection)

    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/")
def login():
    return render_template('login.html')

@app.route("/login",methods=['GET', 'POST'])
def checklogin():
    error = None;
    un=request.form["username"]
    pw = request.form["password"]
    print(un,pw)
    cursor = connection.cursor()
    query="select user_name,password from users where user_name=%s and password=%s"
    data = (un,pw)
    cursor.execute(query, data)
    rows=cursor.fetchall()
    if len(rows)>=1:
        flash("you are successfuly logged in")
        return render_template('logged.html')
    else:
        error = "invalid username or password"
        flash('Wrong username or password')
        return render_template('login.html',error=error)


if __name__ == "__main__":
    print("starting server")
    app.secret_key = 'super secret key'

    app.run(port=5000,debug=True)
