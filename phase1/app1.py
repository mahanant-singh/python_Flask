from flask import Flask, request, redirect, url_for, session, Response

app1 = Flask(__name__)
app1.secret_key = "supersecret"


@app1.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            session["user"] = username  # Store user in session
            return redirect(url_for("welcome"))
        else:
            return Response(
                "Invalid credentials, try again!",
                mimetype="text/plain"
            )

    return """
    <h2>Login Page</h2>
    <form method="POST">
        Username:
        <input type="text" name="username"><br><br>

        Password:
        <input type="password" name="password"><br><br>

        <input type="submit" value="Login">
    </form>
    """


@app1.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session['user']}!</h2>
        <a href="{url_for('logout')}">Logout</a>
        '''

    return redirect(url_for("login"))


@app1.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app1.run(debug=True)