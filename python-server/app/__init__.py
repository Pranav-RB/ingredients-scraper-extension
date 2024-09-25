from flask import Flask # type: ignore
from app.config import Config
from app.main.models import db
from flask_login import LoginManager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skincare.db'
    db.init_app(app)
    login_manager = LoginManager(app)

    # from app.recommedations impor
    # t bp as recommedations_bp
    # app.register_blueprint(recommedations_bp, url_prefix='/recommedations')

    # from app.users import bp as users_bp
    # app.register_blueprint(users_bp, url_prefix='/users')
    
   
    return app