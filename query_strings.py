#!/usr/bin/python3
""" Demonstrating the usage of Query Strings. 

For performing tests, some CURl examples:

    $ curl "http://127.0.0.1:8000/qs?name=Nemo&country=Norway"
"""

from flask import abort, Flask, jsonify, request

__author__ = "@ivanleoncz"


app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
