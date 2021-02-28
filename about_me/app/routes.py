#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Routes"""

from about_me.app import app

@app.route("/")
def index():
    return "Hello there World"


@app.route("/aboutme")
def about_me():
    about_me = {
        "first_name" : "Gary",
        "last_name" : "Newmey",
        "hobby" : "climbing"
    }
    return about_me