#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the value of the X-Request-Id variable
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header['X-Request-Id'])
