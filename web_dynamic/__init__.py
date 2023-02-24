#!/usr/bin/python3
"""Init file for the web_dynamic module"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__)


from web_dynamic.0-hbnb import *
from web_dynamic.1-hbnb import *
from web_dynamic.2-hbnb import *
from web_dynamic.3-hbnb import *
from web_dynamic.4-hbnb import *
from web_dynamic.100-hbnb import *
from web_dynamic.101-hbnb import *
