#!/usr/bin/env python

'''
    For testing requisitions: curl "http://127.0.0.1:8000/hello/?name=IvanLeon"
'''

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask!"

@app.route('/hello/')
def hello():
    name = request.args.get('name')
    return 'Hello, %s !' % name

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
