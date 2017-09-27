from flask import Flask
from flask_security import Security

# project imports
from config import *
from database import get_db

app = Flask(__name__)
app.config.from_object(BaseConfig)
with app.app_context():
    db = get_db()
security = Security(app, db)




