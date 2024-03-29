#!/usr/bin/python3
"""This script that fetches https://intranet.hbtn.io/status
It fetches the URL and displays the value of the X-Request-Id variable found in the header of the response.
The value of this variable is different for each request. 
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
