#!/usr/bin/env python

"""
This template/example demonstrates how to load Jinja2 templates (HTML) with variables.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    message="Jinja2 template message loaded via..."
    return render_template('index.html',title=message)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)
