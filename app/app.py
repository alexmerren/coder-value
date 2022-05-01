"""The app module, containing the app factory function"""
from flask import Flask, render_template, request
from app.github.api import get_single_file_of_repo 

def create_app():
    """ """
    app = Flask(__name__.split(".")[0])

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST" and request.form['username'] != '':
            form = request.form
            response = get_single_file_of_repo(form['username'])
            return render_template("index.html", response=response)
        return render_template('index.html', response=None)

    @app.errorhandler(404)
    def resourceNotFound(e):
        return render_template("404.html"), 404
    return app
