# file where we'll store most of our views/routes
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db 
import json

# we will Blueprints as a way to store our routes
# Blueprint for our views file
views = Blueprint('views', __name__)

# home page
@views.route('/')
def home():
    return render_template("index.html", user=current_user)

# hotels page
@views.route('/hotels')
@login_required
def hotels():
    return render_template("hotels.html", user=current_user)

# rooms page
@views.route('/rooms')
@login_required
def rooms():
    return render_template("rooms.html", user=current_user)

# profile page
@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)



