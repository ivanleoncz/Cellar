#!/usr/bin/python3
""" Main application module, providing access to views/routes. """

from flask import Flask, render_template
from modules import database

__author__ = "@ivanleoncz"

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def f_index():
    return "Welcome to Flask!"


@app.route("/ranking")
def f_ranking():
    data = db_lite.reader()
    return render_template('ranking.html',ranking=data)


if __name__ == "__main__":
    db_lite = database.Lite("ieee.sqlite3")
    db_lite.builder()
    app.run(host="127.0.0.1",port=8000)

