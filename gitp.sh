#!/bin/bash

# Add all files to the staging area
git add .

# Check if there are any changes to commit
if git diff-index --quiet HEAD --; then
    echo "No changes to commit."
    exit 0
fi

# Generate commit message with current timestamp
commit_message="Auto-commit at $(date +'%Y-%m-%d %H:%M:%S')"

# Commit changes with the generated message
git commit -m "$commit_message"

# Push changes to the default remote repository and branch
git push

# Check if the push was successful
if [ $? -eq 0 ]; then
    echo "Push successful."
else
    echo "Error: Push failed."
fi
