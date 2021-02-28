#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Sample App"""

from flask import Flask

app = Flask(__name__)

from about_me.app import routes # must go last