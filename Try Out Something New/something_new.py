from flask import FLask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from time import timedelta
import os
from dotenv import load_dotenv

"""So this project is a random project to let Harini Sridhar know that I like her the way she is, and that she should never worry about regrets in life.
Why does it sound so sad one might ask? well, That's cuz she's going through a lotta stuff at the moment,and as her hun-bun, I want to do something about it.
BUT the matter of the fact is that her parents totally hate the fact that me Harini Sridhar are together. So I essentially can't do anything, because me doing something will
mess up her situation more. Hence I'll be as supportive as I can, but I won't break my promise at any cost: I won't leave[more like I can't].
If she wants to get rid of me she knows how to, and *SIGH* that will be hurtful to me, but that's the only way to get rid of me"""

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=60)
app.secret_key(os.getenv("secret"))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///simple.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 

class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __init__(self, id, name):
        self.id = _id
        self.name = name
        
    def __repr__(self):
        return self.name

@app.route("/")
@app.route("/home")
def home():
    render_template("home.html")

@app.route("/view")
def view():
    render_template("view.html", items=users.query.all())

@app.route("/memories")
def memories():
    pass

if __name__ == "__main__":
    app.run(debug=True)