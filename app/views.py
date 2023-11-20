#!/usr/bin/env python3
"""defines the overall structure of our app"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"], strict_slashes=False)
def home():
    """home page"""
    return render_template("home.html")
