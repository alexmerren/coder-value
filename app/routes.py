from app.github.file import get_single_file_of_repo 
from app.github.loc import get_account_loc 
from flask import Blueprint, render_template, request
import requests_cache

basic = Blueprint('basic', __name__, template_folder="templates")

@basic.route("/", methods=["GET", "POST"])
def index():
    # If there is validation errors, return a page with no info
    if request.method != "POST" or request.form['username'] == '':
        return index_error("Please insert a GitHub username to get started")

    # If the GitHub API fails for some reason, return empty page
    file_response = get_single_file_of_repo(request.form['username'])
    if file_response == None:
        return index_error("There was an error retrieving user file information") 

    loc_response = get_account_loc(request.form['username'])
    if loc_response == None:
        return index_error("There was an error retrieving account statistics")

    # Calculate the cost per line in file
    salary = request.form["salary"] if request.form["salary"] != "" else 0
    file_value = file_response['lines']/loc_response['totalLines']*int(salary)

    return render_template("index.html", 
                           file_response = file_response, 
                           loc_response = loc_response,
                           file_value = f"{file_value:.2f}",
                           error = None)

def index_error(error):
    return render_template('index.html', file_response=None, loc_response=None, file_value=None, error=error)

@basic.errorhandler(404)
def resourceNotFound(e):
    return render_template("404.html"), 404

@basic.errorhandler(500)
def resourceNotFound(e):
    return index_error("There was an error, please try again") 
