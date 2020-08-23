#!/bin/sh

python /src/get_token.py
export REVIEWDOG_GITHUB_API_TOKEN=`cat /src/token.conf`
echo $REVIEWDOG_GITHUB_API_TOKEN
curl -X POST \
     -H "Authorization: token ${REVIEWDOG_GITHUB_API_TOKEN}" \
     -H "Accept: application/json" \
     -H "Content-Type:application/json" \
     -d "{\"body\": \"hello \\\n world!\"}" \
     "https://api.github.com/repos/${DRONE_REPO_OWNER}/${DRONE_REPO_NAME}/issues/${DRONE_PULL_REQUEST}/comments"
