""" File to get lines of code for a user on GitHub API """
from .api import request_with_auth, get_repos_in_time_range 

USERS_TOTALLINES = {}

def get_repository_weekly_commits(repo_name):
    return request_with_auth(f"http://api.github.com/repos/{repo_name}/stats/code_frequency").json()

def get_lines_for_repository(repo_name):
    response = get_repository_weekly_commits(repo_name)
    lines_for_repository = 0
    for commit in response:
        lines_for_repository += commit[1] + commit[2]
    return lines_for_repository

def get_all_repository_lines(username):
    total_lines = 0
    repo_name_list = get_repos_in_time_range(username)
    for repo_name in repo_name_list:
        total_lines += get_lines_for_repository(repo_name)
    return total_lines 

def get_account_loc(username):
    if username in USERS_TOTALLINES:
        return {"totalLines":USERS_TOTALLINES[username]}

    total_lines = get_all_repository_lines(username)
    USERS_TOTALLINES[username] = total_lines 
    return {"totalLines":total_lines}
