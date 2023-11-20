#!/usr/bin/env python3
"""module to define our authetications login, logout and sign up"""
from flask import Blueprint, render_template, flash, request

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """Login page"""
    data = request.form.get
    return render_template("login.html")


@auth.route("/logout", methods=["GET", "POST"], strict_slashes=False)
def logout():
    """Logout of the app"""
    return "<p>Logout</p>"


@auth.route("/sign-up", methods=["GET", "POST"], strict_slashes=False)
def sign_up():
    """signup to the website"""
    if request.method == "POST":
        email = request.form.get("email")
        FullName = request.form.get("fullname") or ""
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if not email or len(email) < 5 or "@" not in email:
            flash("Email must have atleast 5 characters", category="error")
        elif len(FullName) < 7 or not FullName:
            flash("FullNames must have atleast 7 characters", category="error")
        elif password1 != password2:
            flash("Password1 must be equal to password2", category="error")
        elif len(password1) < 7 or len(password2) < 7:
            flash(
                "The Password must be atleast 7 characters long", category="error     "
            )
        else:
            flash("Account created!", category="success")
            pass

    return render_template("sign_up.html")
