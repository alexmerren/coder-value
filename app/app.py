"""The app module, containing the app factory function"""
from flask import Flask, render_template, request
from app.github.file import get_single_file_of_repo 
from app.github.loc import get_account_loc 

def create_app():
    """ Flask app factory """
    app = Flask(__name__.split(".")[0])

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST" and request.form['username'] != '':
            form = request.form
            file_response = get_single_file_of_repo(form['username'])
            loc_response = get_account_loc(form['username'])
            return render_template("index.html", 
                                   file_response = file_response, 
                                   loc_response = loc_response)
        return render_template('index.html', file_response=None, loc_response=None)

    @app.errorhandler(404)
    def resourceNotFound(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internalServerError(e):
        return render_template("500.html"), 500 

    return app

