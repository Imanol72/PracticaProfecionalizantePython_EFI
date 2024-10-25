from .auth_view import auth_bp #Con el punto lo busca en la carpeta, sin busca en la raiz 

def register_blueprints(app):
    app.register_blueprint(auth_bp)