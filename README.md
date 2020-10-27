# ApriorLibrary_Tutorial
Python Aprior Library Tutorial 

**Fork Sync-ing**
Add the remote, call it "upstream":

git remote add upstream https://github.com/whoever/whatever.git

Fetch all the branches of that remote into remote-tracking branches, such as upstream/main or upstream/master:

git fetch upstream

Make sure that you're on your main branch:

git checkout main

Rewrite your main branch so that any commits of yours that aren't already in upstream/main are replayed on top of that other branch:

git rebase upstream/main
source:https://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository

git merge upstream/main