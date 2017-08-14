#!/usr/bin/env python3

""" 
This example/template just captures the Werkzeug loggers,
without modifying any message, just writting to a file.
The generated Traceback are captured by @app.errorhandler
decorator, just to maintain the stdout without any message.

IMPORTANT: in this example/template, the Tracebacks are not
written to the file, although 5xx are registered.

"""

from flask import Flask, jsonify
import logging

app = Flask(__name__)


@app.route("/")
def get_index():
    return "Welcome to Flask! "

@app.route("/data")
def get_hello():
    data = {
             "Name":"Ivan Leon",
             "Occupation":"Software Developer",
             "Technologies":"[Python, Flask, MySQL, Android]"
           }
    return jsonify(data)

@app.route("/error")
def get_json():
    # Intentional non existent variable.
    return non_existent_variable


@app.errorhandler(Exception)
def exceptions(e):
    """ This avoids the generation of Tracebacks on stdout, capturing exceptions. """
    return "Internal Server Error",500


if __name__ == "__main__":
    logging.basicConfig(filename='app.log',format='%(message)s',level=logging.INFO)
    app.run(host="127.0.0.1",port=8000,debug=True)
