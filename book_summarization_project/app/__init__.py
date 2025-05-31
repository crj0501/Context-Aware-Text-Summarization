from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Import and register routes
    from app.routes import initialize_routes
    initialize_routes(app)

    return app
