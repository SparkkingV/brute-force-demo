from flask import Flask, request , render_template_string

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "admin@123"

html_page =  """

    <!DOCTYPE html>
<html>
<head>
    <title>vault</title>
</head>
<body>

<h2>Login Page</h2>

<form action="/login" method="POST">
    <input type="text" name="username" placeholder="Email" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Login</button>
</form>

<p>{{ message }}</p>

</body>
</html>

"""
@app.route("/", methods=["GET","POST"])
def login():
    message = ""
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD :
            message = "LOGIN SUCCESSFUL"
        else:
            message = "LOGIN FAILED"

    return render_template_string(html_page,message=message)

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=1106,debug=True)
