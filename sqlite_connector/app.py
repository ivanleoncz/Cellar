#!/usr/bin/env python

import json
from app_modules import sqlite3mod
from flask import Flask, render_template

app = Flask(__name__)
lite_obj = None


@app.route("/ranking")
def f_ranking():
    db_querier = lite_obj.data_querier()
    return render_template('ranking.html',ranking=db_querier)


if __name__ == "__main__":
    lite_obj = sqlite3mod.Lite("test.db")
    db_builder = lite_obj.data_builder()
    app.run(host="127.0.0.1",port=8000,debug=True)

