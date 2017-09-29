class BaseConfig:
    TITLE = "Felforged Covenant"
    NAVIGATION_LOGGED_OUT = [
        {
            "url": "/register",
            "name": "Register"
        },
        {
            "url": "/login",
            "name": "Login"
        }
    ]
    NAVIGATION_LOGGED_IN = [
        {
            "url": "/profile",
            "name": "Profile"
        },
        {
            "url": "/logout",
            "name": "Logout"
        }
    ]

    SECRET_KEY = "kjsdnf 3weedh ubA &S*YBWFDWEBFdnbf WDEufw897euonAE SD9#@R$&BfdLKFIJH wey8"

    # Flask-SQLAlchemy Config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///./storage/felforged.db"

    # Flask-Security Config
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "pbkdf2"
    SECURITY_LOGIN_USER_TEMPLATE = "./templates/login.html"


class DebugConfig(BaseConfig):
    DEBUG = True
