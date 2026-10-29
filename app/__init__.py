from flask import Flask
from .extensions import appbuilder , db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")
    
    db.init_app(app)
    with app.app_context():
        # db.create_all()
        appbuilder.init_app(app, db.session)
        from . import models
        from .models import Categoria, Ingrediente
        from . import views
        
        # registrar la view de ia
        from .ai.asistente_ai import asistente_bp
        app.register_blueprint(asistente_bp);
    return app

app = create_app()