import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    db.init_app(app)

    # Registro de los Blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    from .admin import admin_bp
    app.register_blueprint(admin_bp)
    from .public import public_bp
    app.register_blueprint(public_bp)
 
    # Manejo de errores personalizados
    register_error_handlers(app)
 
    return app

def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404

    

