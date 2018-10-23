
import os
import random
from flask import Flask, request, session

app = Flask(__name__)

credentials = {"UserName":"ivanleoncz", "PassWord":"p455w0rd"}

messages = [
            "Get some sleep.",
            "Cookies are awesome.",
            "Have a cup of coffee.",
            "Take an umbrella with you.",
            "Do exercises."
           ]

@app.route("/login", methods = ['GET', 'POST'])
def f_login():
    login_form = " \
      <form action='/login' method='post'> \
        <input type='text' name='username' placeholder='Username'></input><br> \
        <input type='password' name='password' placeholder='Password'></input><br> \
        <input type='submit' value='Log In'></input> \
      </form> "
    if request.method == 'GET':
        return login_form
    elif request.method == 'POST':
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


@app.route("/logout", methods = ['GET'])
def f_logout():
    session.pop("IsLogged", None)
    return "Logout -> OK"


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run()
