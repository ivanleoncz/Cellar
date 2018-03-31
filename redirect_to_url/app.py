#!/usr/bin/python3
""" Demonstration of URI redirection. 

Testing redirection:
    $ curl -L http://127.0.0.1:8000/

Taking from "man curl":
    -L, --location
      If the server reports that the requested page has moved to a different 
      location (indicated with a Location: header and a  3XX  response  code),
      this option will make curl redo the request on the new place.
"""

from flask import Flask, redirect

__author__ = "@ivanleoncz"


app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/you_were_redirected')


@app.route("/you_were_redirected")
def redirected():
    return "You were redirected. Congrats :)!"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)
