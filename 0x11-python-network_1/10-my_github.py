#!/usr/bin/python3
"""
Takes GitHub credentials and uses the GitHub API to display the user's id.
Uses Basic Authentication with a personal access token as the password.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: {} <username> <token>".format(sys.argv[0]))

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        data = response.json()
        print(data.get('id'))
    except requests.exceptions.RequestException as e:
        print("None")
