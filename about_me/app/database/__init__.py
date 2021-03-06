#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Database functions"""

from flask import g
from about_me.app import app
import sqlite3

DATABASE = "user.db"

# ---- C O N N E C T   D B
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# ---- C R E A T E   U S E R
def create_user(fn, ln, hobby, fav_food):
    value_tuple = (fn, ln, hobby, fav_food)
    query = """INSERT INTO user(first_name, last_name, hobbies, favorite_food) VALUES(?, ?, ?, ?)"""
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    return last_row_id


# ---- G E T   A L L   U S E R S
def get_all_users():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return results


# ---- G E T   O N E   U S E R S
def get_one_user(user_id):
    cursor = get_db().execute("SELECT * FROM user WHERE id=%s" % user_id, ())
    results = cursor.fetchall()
    cursor.close()
    return results


# ---- U P D A T E   U S E R
def update_user(user_id, values: dict):
    value_string = ",".join("%s=\"%s\"" % (key, val) for key, val in values.items())
    query = """UPDATE user SET %s WHERE id=?""" % value_string
    cursor = get_db()
    cursor.execute(query, (user_id))
    cursor.commit()
    return True


# ---- D E L E T E   U S E R
def delete_user(user_id):
    query = "DELETE FROM user WHERE id=%s" % user_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True


# ---- G E T   A L L   P R O D U C T S
def get_all_prods():
    cursor = get_db().execute("SELECT * FROM products", ())
    results = cursor.fetchall()
    cursor.close()
    return results
