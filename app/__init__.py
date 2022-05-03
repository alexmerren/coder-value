from flask import Flask
from app.routes import basic

def init_app():
    app = Flask(__name__)
    app.register_blueprint(basic)
    return app
