#!/usr/bin/python3
""" Demonstration of redirection, to dynamic URI. """

from flask import Flask, redirect, request, url_for

__author__ = "@ivanleoncz"

app = Flask(__name__)


@app.route('/user/<name>')
def hello_user(name):
    print("Requested URI: ", request.path)
    if name == 'admin':
        return redirect('/admin')
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/admin')
def hello_admin():
    print("Requested URI (redirect): ", request.path)
    return "Hello, Admin!"


@app.route('/guest/<guest>')
def hello_guest(guest):
    print("Requested URI (redirect): ", request.path)
    return "You are a Guest, %s!" % guest


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
