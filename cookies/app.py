#!/usr/bin/env python3

""" Demonstrating cookie management (read/write).  """

from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/read')
def f_read():
    username = request.cookies.get('username')
    if username:
        return "Cookie Present for %s!" % username
    else:
        return "Cookie Not Present..."

@app.route('/write')
def f_write():
    username = "Ivan Leon"
    resp = make_response("<h1> Storing Cookie </h1>")
    resp.set_cookie('username',username)
    return resp

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)

