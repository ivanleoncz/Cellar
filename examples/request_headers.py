#!/usr/bin/python3
""" Demonstration of request headers returned from a request.  """

from flask import Flask, jsonify, request

__author__ = "@ivanleoncz"


app = Flask(__name__)

@app.route("/")
def f_index():
    """ Transforms all request headers into a list for JSON dump. """
    data = []
    for line in request.headers:
        data.append(line)
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
