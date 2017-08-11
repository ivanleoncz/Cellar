#/usr/bin/env python3

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify
from time import strftime
import traceback

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


@app.after_request
def after_request(response):
    # This IF avoids the duplication of registry in the log,
    # since that 500 is already logged via @app.errorhandler.
    if response.status_code != 500:
        ts = strftime('[%Y-%b-%d %H:%M]')
        logger.error('%s %s %s %s %s %s', 
                      ts, 
                      request.remote_addr,
                      request.method, 
                      request.scheme, 
                      request.full_path, 
                      response.status)
    return response

@app.errorhandler(Exception)
def exceptions(e):
    ts = strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                  ts, 
                  request.remote_addr, 
                  request.method,
                  request.scheme, 
                  request.full_path, 
                  tb)
    return "Internal Server Error", 500

if __name__ == '__main__':
    # The maxBytes is set to this number, in order to demonstrate the generation of multiple log files (backupCount).
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
    # getLogger('__name__') - decorators loggers to file / werkzeug loggers to stdout
    # getLogger('werkzeug') - werkzeug loggers to file / nothing to stdout
    logger = logging.getLogger('__name__')
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    app.run(host="127.0.0.1",port=8000)

