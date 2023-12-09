from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# initializing our database
db = SQLAlchemy()
DB_NAME = "database.db"

# function to create our flask app
def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # storing our db into a folder
    db.init_app(app)
    
    # need to register our blueprints in our init file so we can actually visit the routes
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Hotel, Room, Booking
    
    # creating the db
    with app.app_context():
        db.create_all()
        
    # set up the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

