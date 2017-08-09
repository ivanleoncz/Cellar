#!/usr/bin/env python3

from flask import Flask, redirect
import logging

app = Flask(__name__)

@app.route("/")
def f_index():
    return "<h3> Flask is working! </h3>"

@app.route("/data")
def f_data():
    return non_existent_variable

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',format='%(message)s',level=logging.INFO)
    app.run(host="127.0.0.1",port=8000)
