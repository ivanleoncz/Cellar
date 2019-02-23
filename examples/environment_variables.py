
from flask import Flask, jsonify

app = Flask(__name__)

app.config['USERNAME'] = "ivanleoncz"
app.config['APP_MODE'] = "production"


@app.route("/")
def f_index():
    return "Welcome to Flask!<br><br>Check the environment variables \
            <a href='\status'>here</a>."


@app.route("/status")
def f_status():
    data = {
            "username":app.config['USERNAME'],
            "production":app.config['APP_MODE']
            }
    return jsonify(data)


if __name__ == "__main__":
    app.run()


