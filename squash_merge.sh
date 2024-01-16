#!/bin/bash

# Checkout the staging branch and get the latest commit message
git checkout staging
latest_commit_message=$(git log -1 --pretty=%B)

# Checkout the main branch and perform a squash merge
git checkout main
git merge --squash staging

# Add a prefix and use the latest commit message from staging
commit_message="MERGE FROM STAGING: $latest_commit_message"

# Commit with the new message
git commit -m "$commit_message"

# Push to commits to main
git push origin main

# Go back to staging
git checkout staging
# Merge and push, the squashed commit we created in main, into staging history.
git merge main
git push origin staging