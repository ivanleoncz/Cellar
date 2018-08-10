""" Determines if a request was redirected via Reverse Proxy. """

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def f_index():
    request_data = request.environ
    d = {
            "proxy_redirection":None,
            "origin_ip": None,
            "request_data":str(request_data)
        }
    if request_data.get('HTTP_X_FORWARDED_FOR') is not None:
        d["proxy_redirection"] = "Yes"
        d["origin_ip"] = request_data['HTTP_X_FORWARDED_FOR']
        return jsonify(d)
    else:
        d["proxy_redirection"] = "No"
        d["origin_ip"] = request_data['REMOTE_ADDR']
        return jsonify(d)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
