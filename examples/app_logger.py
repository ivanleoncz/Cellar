#/usr/bin/env python3
""" Demonstration of logging feature for a Flask App. """

from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify
from time import strftime

__author__ = "@ivanleoncz"

import logging
import traceback


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def get_index():
    """ Route for / and /index. """
    return "Welcome to Flask! "


@app.route("/data")
def get_data():
    """ Route for /data. """
    data = {
            "Name":"Ivan Leon",
            "Occupation":"Software Developer",
            "Technologies":"[Python, Flask, JavaScript, Java, SQL]"
    }
    return jsonify(data)


@app.route("/error")
def get_nothing():
    """ Route for intentional error. """
    return non_existing_variable # intentional non existent variable


@app.after_request
def after_request(response):
    """ Logging after every request. """
    # This avoids the duplication of registry in the log,
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
    """ Logging after every Exception. """
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
    # maxBytes with small number, in order to demonstrate 
    # the generation of multiple log files (backupCount).
    hand = RotatingFileHandler('app_logger.log', maxBytes=10000, backupCount=3)
    # getLogger(__name__): decorators to file + werkzeug to stdout
    # getLogger('werkzeug'): werkzeug to file + nothing to stdout
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    logger.addHandler(hand)
    app.run(host="127.0.0.1",port=8000)
