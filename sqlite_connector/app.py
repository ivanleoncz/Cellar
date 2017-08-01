#!/usr/bin/env python

import json
from app_modules import sqlite3mod
from flask import Flask, redirect, render_template

app = Flask(__name__)
lite_obj = None

@app.route("/")
@app.route("/index")
def f_index():
    return redirect('/version')


@app.route("/ranking")
def f_ranking():
    db_querier = lite_obj.data_querier()
    return render_template('ranking.html',ranking=db_querier)

@app.route("/version")
def f_sqlite_version():
    db_version = lite_obj.get_version()
    return "<h2 style='position: absolute; top: 30px; left: 50px; text-align: center'> SQLite Version: %s </h2>" % db_version


if __name__ == "__main__":
    lite_obj = sqlite3mod.Lite("test.sqlite3")
    db_builder = lite_obj.data_builder()
    app.run(host="127.0.0.1",port=8000,debug=True)

