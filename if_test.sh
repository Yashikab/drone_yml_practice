#!/bin/bash

if [ $# -eq 0 ]; then
    echo "You have to set at least filename." 1>&2
    exit 1
elif [ $1 = '--test' ]; then
    echo "command is available"
    exit 0
elif [ -e $1 ]; then
    if [[ $1 = *.md ]]; then
        echo "input is markdown"
        curl https://api.github.com/markdown/raw \
            -X "POST" \
            -H "Content-Type: text/plain" \
            -d "$(cat $1)" > target_content
        sed -i -ze "s/\n//g" -e "s/\"/\\\\\\\\\\\\\"/g" target_content
    else
        sed -ze "s/\n/\\\n/g" $1 > target_content
    fi
else 
    echo "file is not found." 1>&2
    exit 1
fi

if [ $# -ge 2 ] && [ $2 = '--skip-token' ]; then
    echo "skip getting token."
else
    echo "get token."
fi

cat target_content

rm target_content
