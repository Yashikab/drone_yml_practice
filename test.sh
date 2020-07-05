#!/bin/sh

python /src/get_token.py
export REVIEWDOG_GITHUB_API_TOKEN=`cat /src/token.conf`
echo $REVIEWDOG_GITHUB_API_TOKEN
curl -X POST \
     -H 'Content-Type:application/json'
     -H "Authorization: token ${REVIEWDOG_GITHUB_API_TOKEN}" \
     -d "{\"body\": \"hello world\"}" \
     https://api.github.com/repos/Yashikab/drone_yml_practice/issues/15/comments
