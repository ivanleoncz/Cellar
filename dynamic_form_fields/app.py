#!/usr/bin/env python

from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "<h3> Flask Running! <h3>"

@app.route('/data', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return "<h3> /data: GET </h3>"
    if request.method == 'POST':
        # here's the raw of form of the ImmutableMultiDict
        print(request.form,"\n")
        # request.form data stored as ImmutableMultiDict is processed just like a normal Dict
        f = request.form
        # iterating over a list of keys, composed by every first position of every tuple inside the dictionary
        for key in f.keys():
            # generates a list of values, based on the key found in the form (can have more than one key w/same name)
            # iterates over each item (value) from the list
            for value in f.getlist(key):
                # print key from the first for and value
                print(key,":",value)
        return "<h3> /data: POST </h3>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)                                   
