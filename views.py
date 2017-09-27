from flask import render_template, redirect, request
from flask_security import current_user

from app import app
from config import BaseConfig
from templates.forms.registrationform import RegistrationForm
from templates.forms.loginform import LoginForm
from database import create_new_user


@app.route("/")
@app.route("/index", methods=("GET", "POST"))
def index():
    if not current_user.is_authenticated:
        return render_template("latest_article.html",
                               navigation=BaseConfig.NAVIGATION_LOGGED_OUT)
    else:
        return render_template("latest_article.html",
                               navigation=BaseConfig.NAVIGATION_LOGGED_IN)


@app.route("/register", methods=("GET", "POST"))
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        values = [
            request.form["email"], request.form["username"], request.form["password"]
        ]
        try:
            create_new_user(values)
        except Exception as e:
            print("New user creation failed.\n{}".format(e))
        return render_template("latest_article.html",
                               navigation=BaseConfig.NAVIGATION_LOGGED_IN)
    else:
        return render_template("register.html",
                               navigation=BaseConfig.NAVIGATION_LOGGED_OUT,
                               form=form)


@app.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        values = []
        return render_template("latest_article.html",
                               navigation=BaseConfig.NAVIGATION_LOGGED_IN)
    else:
        return render_template("login.html",
                               navigation=BaseConfig.NAVIGATION_LOGGED_OUT,
                               form=form)
