#!/usr/bin/python3

"""This  script that fetches https://alx-intranet.hbtn.io/status
It fetches the URL and displays the value of the X-Request-Id variable found in the header of the response.
"""

if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
