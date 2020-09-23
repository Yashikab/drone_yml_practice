# coding utf-8
# python3.7
# ここのテストでは、get_token.py実行後にこれを実行する(module化しない)
# TODO: get_token.pyをモジュール化する

from github import Github
import os

with open('/src/token.conf', 'r') as f:
    access_token = f.read()

g = Github(access_token)

# tutorial
repo_owner = os.getenv("DRONE_REPO_OWNER")
repo_name = os.getenv("DRONE_REPO_NAME")
issue_no = os.getenv("DRONE_PULL_REQUEST")

repo = g.get_repo(f"{repo_owner}/{repo_name}")
issue = repo.get_issue(int(issue_no))
print(issue)
