import requests
from datetime import datetime, timedelta

# GitHub repository details
owner = "your-repo-owner"
repo = "your-repo-name"
token = "your-github-token"  # You can generate a personal access token from GitHub

# Set the time range to the last 24 hours
since = (datetime.utcnow() - timedelta(days=1)).isoformat() + 'Z'

# GitHub API URL
url = f"https://api.github.com/repos/{owner}/{repo}/commits"

# Make the request
headers = {'Authorization': f'token {token}'}
params = {'since': since}
response = requests.get(url, headers=headers, params=params)

# Check the response status and print the commit messages
if response.status_code == 200:
    commits = response.json()
    for commit in commits:
        print(f"Commit: {commit['commit']['message']}")
        print(f"Author: {commit['commit']['author']['name']}")
        print(f"Date: {commit['commit']['author']['date']}\n")
else:
    print(f"Failed to fetch commits: {response.status_code}")
