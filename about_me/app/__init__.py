#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Sample App"""

from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from about_me.app import routes  # must go last