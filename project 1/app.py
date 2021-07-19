from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# a secret key is required to start sessions

app.secret_key = "hello"

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# for permanent sessions we use timedelta and this method below from flask
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

# this class is used to control the Database and save it


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return self.name


@app.route("/")
def home():
    return render_template("home.html", content=["Nikhil", "Harini Sridhar"])


@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())


@app.route("/delete", methods=["GET", "POST"])
def delete():
    for i in users.query.filter_by().all():
        db.session.delete(i)
        db.session.commit()
    flash("You just delelted everything", "info")
    return redirect(url_for("view"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["Name"]
        session["user"] = user
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, None)
            db.session.add(usr)
            db.session.commit()

        flash(f"you have logged in successfully! {user}", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash(f"you have already logged in successfully", "info")
            return redirect(url_for("user"))
        return render_template("login.html")

# "#" sign is used to return to the same page in form


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!", "info")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", user=user)
    else:
        flash(f"you aren't logged in", "info")
        return redirect(url_for("login"))

# to delete once the session is ended


@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"you have logged out successfully! {user}", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
