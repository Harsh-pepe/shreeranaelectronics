from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a strong secret key
# Device responsiveness is typically handled in the HTML and CSS files, not in the Python backend.
# However, you can ensure the backend serves the correct templates or static files if needed.
USERNAME = "admin"
PASSWORD = "password"

def load_products():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_products(products):
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/contactus")
def contact():
    return render_template("form.html")
@app.route("/products")
def get_products():
    return jsonify(load_products())

@app.route("/admin", methods=["GET", "POST"])
def admin():
    session.permanent = True
    if "logged_in" in session:
        return render_template("admin.html")
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == USERNAME and password == PASSWORD:
            session["logged_in"] = True
            session.permanent = True
            return redirect(url_for("admin"))
        return "Invalid credentials, try again!"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

@app.route("/add_product", methods=["POST"])
def add_product():
    if "logged_in" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    products = load_products()
    products.append(data)
    save_products(products)
    return jsonify({"message": "Product added successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
