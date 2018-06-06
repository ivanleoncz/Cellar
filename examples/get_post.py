#!/usr/bin/python3
""" Demonstration of GET/POST requests. 

For performing tests, some CURl examples:

$ curl http://127.0.0.1:8000/index
$ curl http://127.0.0.1:8000/data -d "name=Nemo&country=Norway"
$ curl http://127.0.0.1:8000/all_data -d "name=Nemo&country=Norway&role=Dev"
"""

from flask import abort, Flask, jsonify, request

__author__ = "@ivanleoncz"

app = Flask(__name__)


@app.route('/all_data', methods=['POST'])
def f_data():
    if request.method == "POST":
        print(request.headers)
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        return jsonify(data)
    else:
        abort(405) # aborting: Method Not Allowed


@app.route('/data', methods=['POST'])
def f_report():
    if request.method == 'POST':
        name      = request.form["name"]
        country   = request.form["country"]
        ipaddress = request.remote_addr
        data = ["POST", name, country, ipaddress]
        return jsonify(data)
    else:
        abort(405) # aborting: Method Not Allowed


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
