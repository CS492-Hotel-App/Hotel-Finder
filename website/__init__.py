from flask import Flask

# function to create our flask app
def create_app():
    app = Flask(__name__)
    
    # need to register our blueprints in our init file so we can actually visit the routes
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app

