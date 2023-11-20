#!/usr/bin/env python3
"""module to define our authetications login, logout and sign up"""
from flask import Blueprint, render_template, flash, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """Login page"""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully", category="success")
            else:
                flash("Incorrect Password, try again", category="error")
        else:
            flash("Email does not exist", category="error")
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

        user = User.query.filter_by(email=email).first()
        if user:
            flash("User already exists", category="error")
        elif not email or len(email) < 5 or "@" not in email:
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
            new_user = User(
                email=email,
                fullname=fullname,
                password=generate_password_hash(password1, method="sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("sign_up.html")
