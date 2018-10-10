
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/", methods = ['GET'])
def f_index():
    return render_template("get_parse_json.html")


@app.route("/json", methods = ['GET'])
def f_json():
    d = {"Name":"John Doe", "Country":"Ireland", "Age":34}
    return jsonify(d)


if __name__ == "__main__":
    app.run()
