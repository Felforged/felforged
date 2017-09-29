from flask import render_template, redirect, request, url_for
from flask_login import login_user, login_required, logout_user, current_user
from passlib.hash import pbkdf2_sha256
# internal imports
from app import app, login_manager
import forms
from models import Users, add_user_to_db


def get_nav():
    nav = []
    if current_user.is_authenticated:
        n = [
            {
                "url": "/profile",
                "name": "Profile"
            },
            {
                "url": "/logout",
                "name": "Logout"
            }
        ]
        for n in n:
            nav.append(n)
    else:
        n = [
            {
                "url": "/register",
                "name": "Register"
            },
            {
                "url": "/login",
                "name": "Login"
            }
        ]
        for n in n:
            nav.append(n)
    return nav


@login_manager.user_loader
def get_user(user):
    return Users.query.get(user)


@app.route("/")
@app.route("/index")
def index():
    nav = get_nav()
    return render_template("latest_article.html",
                           navigation=nav)


@app.route("/register", methods=["GET", "POST"])
def register():
    nav = get_nav()
    form = forms.RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        try:
            user = Users(email=form.email.data,
                         username=form.username.data,
                         password=pbkdf2_sha256.hash(form.password.data))
            add_user_to_db(user)
            user.authenticated = True
            login_user(user, remember=True)
            return redirect("/")
        except:
            print("Problem adding user to db.")
            return redirect("/register")
    else:
        return render_template("register.html",
                               navigation=nav,
                               form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    nav = get_nav()
    form = forms.LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = Users.query.filter_by(email=form.email.data).first_or_404()
        if user is not None and pbkdf2_sha256.verify(form.password.data, user.password):
            user.authenticated = True
            login_user(user, remember=True)
            return redirect("/")
        else:
            return redirect("/login")
    else:
        return render_template('login.html',
                               navigation=nav,
                               form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    nav = get_nav()
    form = forms.NewArticleForm(request.form)
    if request.method == "POST" and form.validate():
        user
