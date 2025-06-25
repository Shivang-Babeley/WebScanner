from main import run_recursive_scan
from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        depth = int(request.form["depth"])
        run_recursive_scan(url, max_depth=depth,page_limit=10)

        # Load the resulting report
        with open("reports/output.json") as f:
            data = json.load(f)

        return render_template("result.html", report=data, url=url, depth=depth)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    # this is my main function
