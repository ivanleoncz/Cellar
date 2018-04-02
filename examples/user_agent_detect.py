#!/usr/bin/python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def f_index():
    ua = request.headers.get('User-Agent')
    if "Windows Phone" in ua:
        return "Hello, Windows Phone!\n"
    elif "Android" in ua:
        return "Hello, Android!\n"
    elif "iPad" in ua:
        return "Hello, iPad!\n"
    elif "iPhone" in ua:
        return "Hello, iPhone!\n"
    elif "Windows NT" in ua:
        return "Hello, Windows!\n"
    elif "X11" in ua:
        return "Hello, GNU/Linux!\n"
    elif "Mac OS X" in ua:
        return "Hello, Macintosh!\n"
    elif "curl" in ua:
        return "Hello, CURl!\n"
    else:
        return "Who are you?\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
