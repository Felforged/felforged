from wtforms import Form, StringField, PasswordField, validators, SubmitField


class LoginForm(Form):
    email = StringField(label="Email",
                        validators=[validators.InputRequired(message="Email is required."),
                                    validators.Email(message="Must be an email address.")])
    password = PasswordField(label="Password",
                             validators=[validators.InputRequired()])
    submit = SubmitField(label="Login")
