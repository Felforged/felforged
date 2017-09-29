from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# project imports
from config import *


app = Flask(__name__)
app.config.from_object(BaseConfig)
database = SQLAlchemy(app)
database.create_all()
login_manager = LoginManager()
login_manager.init_app(app)
