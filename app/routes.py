from app.github.file import get_single_file_of_repo 
from app.github.loc import get_account_loc 
from flask import Blueprint, render_template, request

basic = Blueprint('basic', __name__, template_folder="templates")

@basic.route("/", methods=["GET", "POST"])
def index():
    # if there is an error with the request, just return the page with no details
    if request.method != "POST" or request.form['username'] == '':
        return render_template('index.html', file_response=None, loc_response=None, file_value=None)

    # get the file details, the total lines of code, the rounded file value, and present those to the index.html 
    form = request.form
    file_response = get_single_file_of_repo(form['username'])
    if file_response == None:
        return render_template('index.html', file_response=None, loc_response=None, file_value=None)

    loc_response = get_account_loc(form['username'])
    file_value = file_response['lines']/loc_response['totalLines']*int(request.form['salary'])
    rounded_file_value = round(file_value, 2)

    return render_template("index.html", 
                           file_response = file_response, 
                           loc_response = loc_response,
                           file_value = rounded_file_value)

@basic.errorhandler(404)
def resourceNotFound(e):
    return render_template("404.html"), 404

@basic.errorhandler(500)
def internalServerError(e):
    return render_template("500.html"), 500 
