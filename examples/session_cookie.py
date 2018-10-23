
import os
import random
from flask import Flask, request, session, abort

app = Flask(__name__)

credentials = {"UserName":"ivanleoncz", "PassWord":"p455w0rd"}
messages = [
            "Get some sleep.",
            "Cookies are awesome.",
            "Have a cup of coffee."
           ]

@app.route("/login", methods = ['POST'])
def f_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == credentials.get("UserName"):
        if password == credentials.get("PassWord"):
            session["IsLogged"] = True
            return "Login -> OK"
    return "NOK"


@app.route("/message")
def f_message():
    if "IsLogged" in session:
        return random.choice(messages)
    return "You must log in."


@app.route("/logout", methods = ['POST'])
def f_logout():
    session.pop("IsLogged", None)
    return "Logout -> OK"


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run()
