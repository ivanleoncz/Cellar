#!/usr/bin/python3

from flask import Flask, jsonify, request, url_for

app = Flask(__name__)

@app.route('/')
def f_index():
    """
        Recommended approach for testing:
            $ curl -L http://127.0.0.1:5000/?name=your_name
    """
    arg = request.args['name']
    return "Your name: %s" % arg

@app.route('/data')
def f_data():
    """
        Recommended approach for testing:
        $ curl "http://127.0.0.1:5000/data?name=your_name&surname=your_surname"
    """
    args = {k:v for (k,v) in request.args.items()}
    return jsonify(args)

if __name__ == "__main__":
    app.run()
