#!/bin/sh

python /src/get_token.py
export REVIEWDOG_GITHUB_API_TOKEN=`cat /src/token.conf`
echo $REVIEWDOG_GITHUB_API_TOKEN
# curl -X PATCH \
#      -H "Authorization: token ${REVIEWDOG_GITHUB_API_TOKEN}" \
#      -H "Accept: application/vnd.github.v3+json" \
#      -H "Content-Type:application/json" \
#      -d "{\"body\": \"hello world!\"}" \
#      "https://api.github.com/repos/${DRONE_REPO_OWNER}/${DRONE_REPO_NAME}/issues/${DRONE_PULL_REQUEST}/comments/42"
curl \
  -X PATCH \
  -H "Authorization: token ${REVIEWDOG_GITHUB_API_TOKEN}" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/${DRONE_REPO_OWNER}/${DRONE_REPO_NAME}/issues/${DRONE_PULL_REQUEST}/comments/840 \
  -d '{"body":"body"}'
