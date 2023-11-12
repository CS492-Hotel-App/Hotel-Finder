# file to store our 'auth' views/routes like sign up page, login page

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# login page
@auth.route('/login')
def login():
    return render_template("login.html")

# sign up page
@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

