#!/usr/bin/env python3
from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """Login page"""
    return "<h1>Login</h1>"


@auth.route("/logout", methods=["GET", "POST"], strict_slashes=False)
def logout():
    """Logout of the app"""
    return "<p>Logout</p>"


@auth.route("/sign-up", methods=["GET", "POST"], strict_slashes=False)
def sign_up():
    """signup to the website"""
    return "<p>Sign Up</p>"
