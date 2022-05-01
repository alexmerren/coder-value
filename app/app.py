"""The app module, containing the app factory function"""
from flask import Flask, render_template, request
from app.github.api import get_year_of_repos 

def create_app():
    """ """
    app = Flask(__name__.split(".")[0])

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "GET":
            return render_template("index.html", response=None)
        if request.method == "POST":
            form = request.form
            response = get_year_of_repos(form["username"])
            return render_template("index.html", response=response)

    @app.errorhandler(404)
    def resourceNotFound(e):
        return render_template("404.html"), 404
    return app
