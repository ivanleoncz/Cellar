#!/usr/bin/env python

from flask import Flask, redirect

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return redirect('/you_were_redirected')

@app.route("/you_were_redirected")
def redirected():
    return "You were redirected. Congrats :)!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)
