from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flaskext.markdown import Markdown
# project imports
from config import *


app = Flask(__name__)
app.config.from_object(BaseConfig)
# SQLAlchemy - NOTE: models must be imported after db has been initialized!
database = SQLAlchemy(app)
from models import User, Article
database.create_all()
# Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
# Flask-Markdown
Markdown(app)
