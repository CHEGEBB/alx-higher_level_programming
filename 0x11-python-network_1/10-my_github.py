#!/usr/bin/python3
"""This script that takes your Github credentials (username and password) and uses the Github API to display your id
Usage: ./10-my_github.py <username> <password>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
