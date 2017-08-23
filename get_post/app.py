#!/usr/bin/env python3

""" Demonstrating GET and POST methods on Flask. """

from flask import abort, Flask, request

app = Flask(__name__)

@app.route('/')
def f_index():
    return "Welcome to Flask!"

@app.route('/data', methods=['POST'])
def f_report():
    if request.method == 'GET':
        # 405: Method Not Allowed
        abort(405)
    else:
        name = request.form['username']
        return "Hello, %s " % name

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
