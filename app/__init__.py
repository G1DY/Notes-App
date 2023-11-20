#!/usr/bin/env python3
"""module to set up our notes app"""
from flask import Flask
from .views import views
from .auth import auth


def create_app():
    """function that starts our app"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mypassword"

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
