from mainweb.models import Users
from mainweb import app, forms, db
from flask import render_template, redirect, url_for, session, flash, request, json
from werkzeug.security import generate_password_hash as gps
from sqlalchemy import desc

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        if "user" in session:
            LogUser = Users.query.filter_by(username=session["user"]).first()
            jshighscore = request.form["jshighscore"]
            if LogUser.highscore < float(json.loads(jshighscore)):
                LogUser.highscore = float(json.loads(jshighscore))
                db.session.commit()
    return render_template("home.html")


@app.route("/leaderboard")
def leaderboard_page():
    rank = Users.query.order_by(desc(Users.highscore)).limit(10).all()
    number = range(1, 11)
    rank_number = zip(rank, number)
    return render_template("leaderboard.html", rank_number=rank_number)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = forms.RegisterForm()
    if "user" in session:
        flash("You are already logged in!", "danger")
        return redirect(url_for("home_page"))
    else:
        if form.validate_on_submit():
            CreateUser = Users(
                username=form.username.data,
                email=form.email.data,
                password=gps(form.password1.data),
                highscore=0
            )
            db.session.add(CreateUser)
            db.session.commit()
            flash("Account succesfully created!", "success")
            return redirect(url_for("login_page"))
        elif form.errors != {}:
            for ErrMsg in form.errors.values():
                flash(str(ErrMsg)[2:-2], "danger")
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = forms.LoginForm()
    if "user" in session:
        flash("You are already logged in!", "danger")
        return redirect(url_for("home_page"))
    else:
        if form.validate_on_submit():
            LogUser = Users.query.filter_by(username=form.username.data).first()
            if LogUser and LogUser.cps(passcheck=form.password.data):
                session["user"] = LogUser.username
                flash(f"Successfully logged in as {LogUser.username}", "success")
                return redirect(url_for("home_page"))
            else:
                flash("Username and password are not match", "danger")
        elif form.errors != {}:
            for ErrMsg in form.errors.values():
                flash(str(ErrMsg)[2:-2], "danger")
        return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
        flash("You have been logged out!", "success")
        return redirect(url_for("home_page"))
    else:
        flash("You have to login first!", "danger")
        return redirect(url_for("login_page"))
