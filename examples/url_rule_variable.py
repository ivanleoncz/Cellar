#!/usr/bin/python3

from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def f_index():
    return redirect("/home/ivanleoncz")

@app.route("/home/<usr>")
def f_home(usr):
    return "<h1>Hello, %s! </h1>" % usr

if __name__ == "__main__":
    app.run()
