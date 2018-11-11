# app/__init__.py
"""File that has the routes for the api """
import os
import random
from flask_api import FlaskAPI
from flask import request, jsonify, make_response, abort

# local import
from instance.config import app_config


def create_app(config_name):
    """Initialize the flask application"""
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')


#***************************************Fetch all parcel delivery orders & Make a new parcel delivery order

# import the authentication blueprint and register it on the app
    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app