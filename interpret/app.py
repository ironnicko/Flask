from flask import Flask, render_template, request, redirect, url_for
from datetime import timedelta
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        code = request.form['code']
        print(code)
        try:
            ret = eval(code)
        except Exception as e:
            ret = e
        print(ret)
        return render_template("output.html", context=ret)


if __name__ == '__main__':
    app.run(debug=True)
