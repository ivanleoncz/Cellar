#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    message="Jinja2 template message loaded via..."
    return render_template('index.html',title=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
