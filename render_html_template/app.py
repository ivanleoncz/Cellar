#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)

app.config(Debug=true)

@app.route("/")
def index():
    message="Template was loaded"
    return render_template('index.html',msg=message)
