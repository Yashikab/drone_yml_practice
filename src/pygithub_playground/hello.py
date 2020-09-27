# coding utf-8
# python3.7
# ここのテストでは、get_token.py実行後にこれを実行する(module化しない)

from gettoken import GetToken
from github import Github
import os
import subprocess

gt = GetToken()
access_token = gt.make_auth_header()

# with open('/src/token.conf', 'r') as f:
#     access_token = f.read()

g = Github(access_token)

# tutorial
repo_owner = os.getenv("DRONE_REPO_OWNER")
repo_name = os.getenv("DRONE_REPO_NAME")
issue_no = os.getenv("DRONE_PULL_REQUEST")

repo = g.get_repo(f"{repo_owner}/{repo_name}")
issue = repo.get_issue(int(issue_no))

pr = issue.as_pull_request()

comment_list = list(issue.get_comments())
comment_list += list(pr.get_review_comments())

dog_marker = \
    '<sub>reported by [reviewdog](https://github.com/reviewdog/reviewdog) '\
    ':dog:</sub>'

for comment in comment_list:
    print(comment.id, comment.body)
    if dog_marker in comment.body:
        comment.delete()


os.environ["REVIEWDOG_GITHUB_API_TOKEN"] = access_token
cmd1 = ["flake8", "./src/"]
cmd2 = [
    "reviewdog",
    "-reporter=github-pr-review",
    "-f=pep8",
    "-diff=\"git diff master\""]
pipe = subprocess.Popen(
    cmd1,
    stdout=subprocess.PIPE
)
reviewdog_result = subprocess.run(
    cmd2,
    stdin=pipe.stdout,
    stdout=subprocess.PIPE
)

print(reviewdog_result.stdout.decode().split('\n'))
