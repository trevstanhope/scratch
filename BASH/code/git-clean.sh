#!/bin/sh
# Flush changes to a repository

# Refresh repository
git pull

# Clear tmp~ and #BUFFER# files
git rm -r *~ \#*#

# Commit changes upstream
git add --all
read -p "enter commit message: " MESSAGE
git commit --all -m "$MESSAGE"
git push
exit
