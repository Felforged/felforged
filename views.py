from flask import render_template, redirect, request, url_for
from flask_login import login_user, login_required, logout_user, current_user
from passlib.hash import pbkdf2_sha256
# internal imports
from app import app, login_manager
import forms
import config
from models import User, add_user_to_db, Article, add_article_to_db


def get_nav():
    nav = []
    if current_user.is_authenticated:
        n = config.BaseConfig.NAVIGATION_LOGGED_IN
        for n in n:
            nav.append(n)
    else:
        n = config.BaseConfig.NAVIGATION_LOGGED_OUT
        for n in n:
            nav.append(n)
    return nav


@login_manager.user_loader
def get_user(user):
    return User.query.get(user)


@app.route("/")
@app.route("/index")
def index():
    nav = get_nav()
    try:
        art = Article.query.order_by(Article.published).first_or_404()
        if art is not None:
            return render_template("latest_article.html",
                                   navigation=nav,
                                   article=art)
    except:
        return render_template("latest_article.html",
                               navigation=nav)


@app.route("/register", methods=["GET", "POST"])
def register():
    nav = get_nav()
    form = forms.RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        try:
            user = User(email=form.email.data,
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
        try:
            user = User.query.filter_by(email=form.email.data).first_or_404()
            if user is not None and pbkdf2_sha256.verify(form.password.data, user.password):
                user.authenticated = True
                login_user(user, remember=True)
                return redirect("/")
            else:
                return redirect("/login")
        except:
            return render_template('login.html',
                                   navigation=nav,
                                   form=form)
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
    user = User.query.filter_by(id=current_user.id).first_or_404()
    if user.role == "admin":
        print(user.role)
        form = forms.NewArticleForm(request.form)
        if request.method == "POST" and form.validate():
            art = Article(title=form.title.data,
                          content=form.text.data,
                          draft=form.draft.data,
                          tags=form.tags.data,
                          author=current_user.username)
            print(art)
            add_article_to_db(art)
            print("adding to db?")
            return redirect("/")
        else:
            return render_template("editor.html",
                                   navigation=nav,
                                   form=form)
    else:
        return redirect("/")
