class BaseConfig:
    TITLE = "Felforged Covenant"
    NAVIGATION_DEBUG = [
        {
            "url": "/register",
            "name": "Register"
        },
        {
            "url": "/login",
            "name": "Login"
        },
        {
            "url": "/profile",
            "name": "Profile"
        },
        {
            "url": "/logout",
            "name": "Logout"
        }
    ]
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


class DebugConfig(BaseConfig):
    DEBUG = True
