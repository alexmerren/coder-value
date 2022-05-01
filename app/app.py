"""The app module, containing the app factory function"""
from flask import Flask, render_template

def create_app():
    """ """
    app = Flask(__name__.split(".")[0])

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.errorhandler(404)
    def resourceNotFound(e):
        return render_template("404.html"), 404
    return app
