#!/usr/bin/env python3
from flask_login import UserMixin
from sqlalchemy import func
from flask import current_app as app
from . import db


class Note(db.Model):
    """defines Note schema"""

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(5000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    """defines user schema"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))
    fullname = db.Column(db.String(250))
    notes = db.relationship("Note")
