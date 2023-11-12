# file to store our 'authorization' views/routes like sign up page, login page, logout

from flask import Blueprint, render_template

# we will Blueprints as a way to store our routes
# Blueprint for our auth file
auth = Blueprint('auth', __name__)

# login page
@auth.route('/login')
def login():
    return render_template("login.html")

# sign up page
@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

