#!/usr/bin/python3
""" Demonstration of request headers returned from a request.  """

from flask import Flask, jsonify, request

__author__ = "@ivanleoncz"

app = Flask(__name__)

@app.route("/headers")
def f_headers():
    """ Transforms all request headers into a list for JSON document. """
    data = []
    # request.headers returns a string which in the following lines
    # is processed and stored as list, for exposure as JSON document.
    # This data is public and it's related to the request only, without
    # exposing any other data from the CGI environment that supports Flask.
    for line in request.headers:
        data.append(line)
    return jsonify(data)

@app.route("/environ")
def f_environ():
    # Without reprocessing ALL VALUES from request.environ dict,
    # it's not possible to deliver it as JSON document:
    # some values (not keys) can't be processed by jsonify(), json.dumps().
    # The data exposed here, must no be exposed to a public via requests,
    # since that is sensitive data about the CGI environment that is
    # supporting Flask.
    return str(request.environ)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
