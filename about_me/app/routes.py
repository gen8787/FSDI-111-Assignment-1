#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Routes"""

from about_me.app import app
from about_me.app.database import *
from flask import request, render_template


# ---- I N D E X
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# A B O U T   M E
@app.route("/aboutme")
def about_me():
    about_me = {
        "first_name": "Gary",
        "last_name": "Newmey",
        "hobby": "climbing"
    }
    return render_template("about.html", about=about_me)


# ---- A D D   U S E R
@app.route("/users/add", methods=["POST"])
def add_user():
    user_data = request.json
    new_id = create_user(
        user_data.get("fn"),
        user_data.get("ln"),
        user_data.get("hobby"),
        user_data.get("fav_food")
    )

    return {"ok": True, "message": "Success", "new_id": new_id}


# ---- A L L   U S E R S
@app.route("/users")
def all_users():
    out = get_all_users()
    return str(out)


# ---- O N E   U S E R S
@app.route("/user/<uid>")
def one_user(uid):
    out = get_one_user(uid)
    return str(out)


# ---- E D I T   U S E R 
@app.route("/user/<uid>/edit", methods=["PUT"])
def edit_user(uid):
    user_data = request.json
    out = update_user(uid, user_data)
    return {"ok": out, "message": "Updated"}


# ---- D E L E T E   U S E R 
@app.route("/user/<int:uid>/remove", methods=["DELETE"])
def remove_user(uid):
    out = delete_user(uid)
    return str(out)


# ---- A G E N T
@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s </p>" % user_agent


# ---- S U M   1   TO   N U M
@app.route("/sums/<int:num>")
def sum(num):
    total = 0
    for n in range(num + 1):
        total += n

    return render_template("sums.html", number = num, total = num(num + 1) / 2)


# ---- A L L   P R O D U C T S
@app.route("/products")
def scan_prods():
    out = get_all_prods()
    return render_template("products.html", products=out)