from flask import Flask, render_template
import json
import os

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "data.json")
with open(DATA_PATH) as f:
    DATA = json.load(f)


@app.route("/")
def index():
    return render_template("index.html", data=json.dumps(DATA))


if __name__ == "__main__":
    app.run(debug=True)
