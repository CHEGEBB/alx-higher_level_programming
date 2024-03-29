import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()

print(html)


req = urllib.request.Request('http://python.org/')
print(req)
with urllib.request.urlopen(req) as response:
    the_page = response.read()

print(the_page)
