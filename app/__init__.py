#!/usr/bin/env python3
"""sets up and runs our notes app"""
from flask import Flask
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy
from .models import User, Note
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    """function that starts our app"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mypassword"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    create_database(app)

    return app


def create_database():
    """creates database"""
    if not path.exists("app/" + DB_NAME):
        db.create_all(app=app)
