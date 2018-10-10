#!/usr/bin/python3

from flask import Flask, jsonify, request
from user_agents import parse

app = Flask(__name__)


@app.route('/')
def f_index():
    return "<h1> Flask is alive! </h1>"

@app.route("/ua")
def f_ua():
    user_agent = parse(request.headers.get('User-Agent'))
    devices = {}
    devices["pc"] = user_agent.is_pc
    devices["mobile"] = user_agent.is_mobile
    devices["tablet"] = user_agent.is_tablet
    ua = {}
    brand = lambda x: "Unknown" if x is None else user_agent.device.brand
    family = lambda x: "Unknown" if x is "Other" else user_agent.device.family
    ua["browser"] = user_agent.browser.family
    ua["os"] = user_agent.os.family
    ua["device_brand"] = brand(user_agent.device.brand)
    ua["device_family"] = family(user_agent.device.family)
    ua["device_type"] = [k for k,v in devices.items() if v == True][0]
    print("Dictionary:", ua)
    return jsonify(ua)


if __name__ == "__main__":
    app.run()
