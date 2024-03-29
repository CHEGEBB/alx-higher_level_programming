#!/usr/bin/python3
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content_type = type(response.text).__name__
    print("Body response:")
    print("\t- type:", content_type)
    print("\t- content:", response.text)
