""" File to add authentication and interact with the GitHub API """
import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta

# Request Authentication
GITHUB_USERNAME = "alexmerren"
GITHUB_TOKEN = "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"
# Control size of response from get_year_of_repos()
MAX_REPOS_PER_PAGE = 100
AMOUNT_OF_DAYS_AGO = 365 

def request_with_auth(url):
    """ Wraps HTTP Request with GitHub authentication """
    return requests.get(url, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))

def get_repos_from_url(username):
    return request_with_auth(f"http://api.github.com/users/{username}/repos?per_page={MAX_REPOS_PER_PAGE}&sort=pushed").json()

def get_repos_in_time_range(username):
    """ Go through the repos that have the last pushed changes at least a year ago """
    names_of_repos = []
    repo_list = get_repos_from_url(username)
    for repo in repo_list:
        date = datetime.strptime(repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")
        if datetime.now() - timedelta(days=AMOUNT_OF_DAYS_AGO) < date:
            names_of_repos.append(repo["full_name"])

    return names_of_repos 
