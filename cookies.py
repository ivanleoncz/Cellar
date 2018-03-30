#!/usr/bin/python3

""" Demonstration of cookie management.  """

from flask import Flask, make_response, request

__author__ = "@ivanleoncz"

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def f_index():
    return "Welcome to Flask!"


@app.route('/write')
def f_write():
    """ Builds a response with a configured cookie. """
    username = "ivanleoncz"
    resp = make_response("<h1> Storing Cookie </h1>")
    resp.set_cookie('username',username)
    return resp


@app.route('/read')
def f_read():
    """ Searches for a cookie """
    username = request.cookies.get('username')
    if username:
        return "Cookie Present for %s!" % username
    else:
        return "Cookie Not Present..."


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)

