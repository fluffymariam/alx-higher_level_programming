#!/usr/bin/python3
"""
Lists 10 most recent commits of a GitHub repository.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: {} <repository_name> <owner_name>".format(sys.argv[0]))

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo_name)

    try:
        response = requests.get(url)
        commits = response.json()

        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get('author', {}).get('name', 'Unknown Author')
            print("{}: {}".format(sha, author_name))

    except requests.exceptions.RequestException as e:
        sys.exit("Error: {}".format(e))
