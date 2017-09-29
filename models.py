from datetime import datetime
# internal imports
from app import database as db


class Users(db.Model):
    """
    This is the user object that gets inserted into our users.db
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.String, default="user")
    banned = db.Column(db.Boolean, default=False)
    joined = db.Column(db.DateTime, default=datetime.now())
    password = db.Column(db.String(255), nullable=False)
    articles = db.relationship("Articles", backref="author", lazy=True)

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<User %r>" % self.username


def add_user_to_db(user):
    db.session.add(user)
    db.session.commit()


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), db.ForeignKey("users.username"), nullable=False)
    filepath = db.Column(db.String(255), default="./articles", nullable=False)
    draft = db.Column(db.Boolean, default=False)
    published = db.Column(db.DateTime, default=datetime.now())
    tags = db.Column(db.String(255))
