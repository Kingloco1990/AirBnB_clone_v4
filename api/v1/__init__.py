#!/usr/bin/python3
"""Init file for views module"""
from flask import Blueprint


app_v1 = Blueprint('app_v1', __name__, url_prefix='/api/v1')


from api.v1.app import *
