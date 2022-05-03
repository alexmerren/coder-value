""" File to get file information from GitHub API """
import json
import os

from random import randint
from .api import request_with_auth, get_repos_from_url, get_repos_in_time_range 

ACCEPTED_FILETYPES = (".go", ".py", ".js", ".cpp", ".c", ".html", ".java", ".ts", ".rb", ".php")
REJECTED_DIRECTORIES = ("vendor", "mocks", "venv")

def get_random_repo_from_list(repo_list):
    random_number = randint(0, len(repo_list)-1)
    return repo_list[random_number]

def get_contents_of_repo(repo_name):
    return request_with_auth(f"http://api.github.com/repos/{repo_name}/git/trees/main?recursive=1").json()

def pick_random_filepath(repo):
    valid_files = []
    if "tree" not in repo:
        return None

    for file_info in repo["tree"]:
        if file_info["path"].endswith(ACCEPTED_FILETYPES) and not file_info["path"].startswith(REJECTED_DIRECTORIES):
            valid_files.append(file_info["path"])

    if len(valid_files) == 0:
        return None

    random_number = randint(0, len(valid_files)-1)
    return valid_files[random_number] 

def get_contents_of_file(repo_name, path):
    file_content = request_with_auth(f"http://raw.githubusercontent.com/{repo_name}/main/{path}").text
    return file_content

def get_single_file_of_repo(username):
    repo_name_list = get_repos_in_time_range(username)
    random_repo_name = get_random_repo_from_list(repo_name_list)
    random_repo_contents = get_contents_of_repo(random_repo_name)
    random_file_path = pick_random_filepath(random_repo_contents)
    if random_file_path == None:
        return None

    random_file_contents = get_contents_of_file(random_repo_name, random_file_path)
    file_line_count = random_file_contents.count("\n")

    return {"filename":f"{random_repo_name}/{random_file_path}",
            "language":os.path.splitext(random_file_path)[1][1:],
            "content":random_file_contents,
            "lines":file_line_count,
           }
