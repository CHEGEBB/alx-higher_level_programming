#!/usr/bin/python3
"""Module for sending a POST request with an email."""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
