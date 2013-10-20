#!/bin/sh
# Trevor Stanhope
# Upload files in current directory to riak cluster.
for file in $(echo *.mp3); 
do  curl -X PUT HTTP://127.0.0.1:8098/riak/songs/${file} -H "Content-type: audio/mpeg" --data-binary @${file}; 
done
