import requests
import json
from datetime import datetime, timedelta

MAX_REPOS_PER_PAGE = 100

def check_user_exists(username):
    res = requests.get(f"http://api.github.com/users/{username}")
    if res.status_code == 200:
        return res.json()
    else:
        return None

def get_year_of_repos(username):
    # Get the number of repos that a user owns, we will use this to go through
    # all the pages of their repos.
    user_response = requests.get(f"http://api.github.com/users/{username}").json()
    number_of_repos = user_response['public_repos']
    number_of_pages_of_repos = number_of_repos % MAX_REPOS_PER_PAGE 
    for page_number in range(number_of_pages_of_repos):

        repos_response = requests.get(f"http://api.github.com/users/{username}/repos?per_page={MAX_REPOS_PER_PAGE}&page={page_number}").json()
        for repo in repos_response:
            date = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
            if datetime.now() - timedelta(days=365) < date:
                print(f"{repo['name']}: {date}")


    # res_data = res.json()
    output_data = {}
    return output_data
