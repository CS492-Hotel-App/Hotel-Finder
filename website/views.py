# file where we'll store most of our views/routes

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# home page
@views.route('/')
def home():
    return render_template("home.html")

# hotels page
@views.route('/hotels')
def hotels():
    return render_template("hotels.html")

# rooms page
@views.route('/rooms')
def rooms():
    return render_template("rooms.html")

# profile page
@views.route('/profile')
def profile():
    return render_template("profile.html")



