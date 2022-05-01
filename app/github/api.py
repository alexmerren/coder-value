""" This is the main interaction point for the GitHub API """
import requests
import json
import base64
import cProfile

from requests.auth import HTTPBasicAuth
from random import randint
from datetime import datetime, timedelta

# TODO: Make these into environment variables 
GITHUB_USERNAME = "alexmerren"
GITHUB_TOKEN = "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"

MAX_REPOS_PER_PAGE = 100
AMOUNT_OF_DAYS_AGO = 365 / 4 
ACCEPTED_FILETYPES = (".go", ".py", "js")
REJECTED_DIRECTORIES = ("vendor/", "mocks/")

def request_with_auth(url):
    """ Wraps HTTP Request with GitHub authentication """
    return requests.get(url, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))

def get_year_of_repos(username):
    """ Go through the repos that have the last pushed changes at least a year ago """
    names_of_repos = []
    repos_response = request_with_auth(f"http://api.github.com/users/{username}/repos?per_page={MAX_REPOS_PER_PAGE}").json()
    for repo in repos_response:
        date = datetime.strptime(repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")
        if datetime.now() - timedelta(days=AMOUNT_OF_DAYS_AGO) < date:
            names_of_repos.append(repo["full_name"])

    return names_of_repos 

def get_contents_of_repo(repo_name):
    """ Get the git tree of a repository """
    return request_with_auth(f"http://api.github.com/repos/{repo_name}/git/trees/main?recursive=1").json()

def pick_semi_random_filepath(repo):
    """ 
    Go through the files in a git tree and reject them if they are in a
    certain directory, and accept them if they have a certain extension 
    """
    valid_files = []
    for file in repo["tree"]:
        if file["path"].endswith(ACCEPTED_FILETYPES) and not file["path"].startswith(REJECTED_DIRECTORIES):
            valid_files.append(file["path"])

    random_number = randint(0, len(valid_files)-1)
    return valid_files[random_number] 

def get_contents_of_file(repo_name, path):
    """ Get the contents of a file using the raw.githubusercontent.com URL """
    file_content = request_with_auth(f"http://raw.githubusercontent.com/{repo_name}/main/{path}").text
    return file_content

def get_single_file_of_repo(username):
    """ 
    Main entry point of the github api that we want to do, getting a random
    file in a repo from the last year
    """
    # Get a list of all the repos that have been worked on in the past year
    names_of_repos = get_year_of_repos(username)

    # Pick a random one out of that list and get the file tree for that repository
    random_number = randint(0, len(names_of_repos)-1)
    random_repo_name = names_of_repos[random_number]
    random_repo_contents = get_contents_of_repo(random_repo_name)

    # Pick a random file within that file tree, and get the filepath for that file. 
    random_file_path = pick_semi_random_filepath(random_repo_contents)

    # Get the contents for the random filepath that was chosen.
    file_contents = get_contents_of_file(random_repo_name, random_file_path)

    return {f"{random_repo_name}/{random_file_path}":file_contents}
