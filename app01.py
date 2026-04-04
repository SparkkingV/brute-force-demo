from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# 🔐 Correct credentials
REAL_USER = "vikashsharan2010@gmail.com"
REAL_PASS = "12345678"

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == REAL_USER and password == REAL_PASS:
        return "Login Successful"
    else:
        return "Login Failed"

app.run(debug=True)