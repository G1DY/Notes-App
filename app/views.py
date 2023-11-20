#!/usr/bin/env python3
from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"], strict_slashes=False)
def home():
    """home page"""
    return "<h1>Test</h1>"
