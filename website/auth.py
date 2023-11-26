# file to store our 'authorization' views/routes like sign up page, login page, logout

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

# we will Blueprints as a way to store our routes
# Blueprint for our auth file
auth = Blueprint('auth', __name__)

# login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):     # checks if the password entered matches the hashed password...
                # flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.profile'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)

# logout
@auth.route('/logout')
# @login_required         # user cannot access this page unless they are logged in 
def logout():
    logout_user()
    return redirect(url_for('views.home'))

# sign up page
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first() # this checks if the email already exists in our db
        
        # validating the input
        if user:
            flash("Email already exists", category="error")        
        elif len(email) < 4:
            flash('Email must be greater than three characters.', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 5:
            flash('Password must be at least five characters', category='error')
        else:
            # entered all valid data, add user to db... hash the users password so it's not stored in plain text
            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))
            
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            
            return redirect(url_for('views.profile'))      # redirects the user to the home page after successfully signing up
            
        
    
    return render_template("sign_up.html", user=current_user)

