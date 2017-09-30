from wtforms import Form, StringField, PasswordField, validators, SubmitField, HiddenField, \
    BooleanField, TextAreaField
from urllib.parse import urlparse, urljoin
from flask import request, url_for, redirect


class RegistrationForm(Form):
    email = StringField(label="Email",
                        validators=[validators.InputRequired(message="Email is required."),
                                    validators.Email(message="Must be an email address.")])
    username = StringField(label="Username",
                           validators=[validators.InputRequired(message="A username is required.")])
    password = PasswordField(label="Password",
                             validators=[validators.InputRequired(),
                                         validators.Length(min=10,
                                                           max=255,
                                                           message="Password must be between 10 and"
                                                                   " 255 characters.")])
    conf_password = PasswordField(label="Confirm Password",
                                  validators=[validators.InputRequired(),
                                              validators.EqualTo("password",
                                                                 message="Passwords do not match.")])
    submit = SubmitField(label="Register")


class LoginForm(Form):
    email = StringField(label="Email",
                        validators=[validators.InputRequired(message="Email is required."),
                                    validators.Email(message="Must be an email address.")])
    password = PasswordField(label="Password",
                             validators=[validators.InputRequired()])
    submit = SubmitField(label="Login")


class NewArticleForm(Form):
    title = StringField("Title")
    text = TextAreaField("Text")
    tags = StringField("Tags")
    draft = BooleanField("Draft?", default=False)
    submit = SubmitField("Submit")
