import sqlite3
from flask import g
from passlib.hash import pbkdf2_sha256


database = "./storage/users.sqlite"


def get_db():
    db = sqlite3.connect(database)
    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def create_new_user(values):
    email = values[0]
    username = values[1]
    hashed_pass = pbkdf2_sha256.hash(values[2])
    db = get_db()
    cur = db.cursor()
    insertion_string = "INSERT INTO users (email, password, username, role) VALUES(?, ?, ?,?);"
    try:
        cur.execute(insertion_string, (email, username, hashed_pass, "user"))
        db.commit()
        close_connection()
    except sqlite3.Error as e:
        print("ERROR: YOU FUCKED UP!\n{}".format(e))


def close_connection():
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
