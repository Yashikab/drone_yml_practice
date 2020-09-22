# coding utf-8
# python3.7
# ここのテストでは、get_token.py実行後にこれを実行する(module化しない)
# TODO: get_token.pyをモジュール化する

from github import Github

with open('/src/token.conf', 'r') as f:
    access_token = f.read()

g = Github(access_token)

# tutorial
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))
