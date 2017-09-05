#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def f_index():
    return str(request.headers)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
