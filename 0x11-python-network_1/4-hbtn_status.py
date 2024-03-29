#!/usr/bin/python3
"""This script fetches https://intranet.hbtn.io/status.
It fetches the URL and displays the type of the response body and the content of the response body.
The content should be utf-8 decoded.
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
