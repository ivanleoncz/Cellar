#!/usr/bin/python3
""" Demonstration of GET/POST requests, including Query Strings. 

For performing tests, some CURl examples:

$ curl http://127.0.0.1:8000/index
$ curl "http://127.0.0.1:8000/qs?name=Nemo&country=Norway"
$ curl http://127.0.0.1:8000/post -d "name=Nemo&country=Norway"
"""

from flask import abort, Flask, jsonify, request

__author__ = "@ivanleoncz"


app = Flask(__name__)

@app.route('/index', methods=['GET'])
def f_index():
    if request.method == 'GET':
        return "Welcome to Flask!"
    else:
        abort(405) # aborting: Method Not Allowed


@app.route('/qs', methods=['GET'])
def f_data():
    if request.method == 'GET':
        if len(request.args) == 0:
            return "Query string Not Found! "
        else:
            name    = request.args.get('name')
            country = request.args.get('country')
            ipaddress = request.remote_addr 
            data = ["Query String", name, country, ipaddress]
            return jsonify(data)
    else:
        abort(405) # aborting: Method Not Allowed


@app.route('/post', methods=['POST'])
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
