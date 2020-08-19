#!/bin/bash

# TODO: markdownにする
if [ $# -ne 1 ]; then
    echo "input target file" 1>&2
    exit 1
elif [ $1 = '--test' ]; then
    echo "command is available"
    exit 0
elif [[ $1 = *.md ]]; then
    echo "input is markdown"
    curl https://api.github.com/markdown/raw \
        -X "POST" \
        -H "Content-Type: text/x-markdown" \
        -d "$(cat $1)"
fi