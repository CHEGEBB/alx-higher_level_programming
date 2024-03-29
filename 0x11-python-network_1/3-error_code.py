#!/usr/bin/python3
""" This script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)."""
if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
