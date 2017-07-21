#!/usr/bin/env python

from flask import Flask, redirect, request, url_for

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    print("\nRequested URL Redirect: ",request.path)
    return "Hello, Admin!"

@app.route('/guest/<guest>')
def hello_guest(guest):
    print("\nRequested via Redirect: ",request.path)
    return "You are a Guest, %s!" % guest


@app.route('/user/<name>')
def hello_user(name):
    print("\nRequested via Browser: ",request.path)
    if name =='admin':
        return redirect('/admin')
    else:
        return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)
