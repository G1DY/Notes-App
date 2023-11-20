#!/usr/bin/env python3
"""sets up and runs our notes app"""
from flask import Flask
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy
from .models import User, Note
from os import path
from flask_login import LoginManager

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

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """validate user from db"""
        return User.query.get(int(id))

    return app


def create_database():
    """creates database"""
    if not path.exists("app/" + DB_NAME):
        with app.app_context():
            db.create_all()
