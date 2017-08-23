#!/usr/bin/env python3

""" Demonstrating GET and POST methods on Flask. """

from flask import abort, Flask, jsonify, request

app = Flask(__name__)

report = { "Date":"Aug,22 2017", "Service":"Web Server", "IPs":['201.39.23.231','133.42.59.3','23.3.48.234'] }

@app.route('/')
def f_index():
    return "Welcome to Flask!"

@app.route('/data', methods=['POST'])
def f_data():
    if request.method == 'GET':
        # 405: Method Not Allowed
        abort(405)
    else:
        name = request.form['username']
        return "Hello, %s " % name

@app.route('/report', methods=['GET'])
def f_report():
    if request.method == 'POST':
        # 405: Method Not Allowed
        abort(405)
    else:
        return jsonify(report)



if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
