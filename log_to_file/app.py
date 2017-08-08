#!/usr/bin/env python

from flask import Flask, redirect
import logging

app = Flask(__name__)

@app.route("/")
def index():
    return "<h3> Flask is working! </h3>"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',format='%(message)s',level=logging.DEBUG)
    app.run(host="127.0.0.1",port=8000)
