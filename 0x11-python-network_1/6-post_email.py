#!/usr/bin/python3
"""This Module for sending a POST request with an email.
It takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
