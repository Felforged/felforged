from wtforms import Form, StringField, PasswordField, validators, SubmitField


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
