# 0x11. Python - Network #1

## Project Descriptions

### 0-hbtn_status.py

A Python script that fetches the status of [https://alx-intranet.hbtn.io] using the urllib package and displays the response body.

### 1-hbtn_header.py

A Python script that takes a URL as input, sends a request, and displays the value of the X-Request-Id variable found in the response header using urllib and sys packages.

### 2-post_email.py

A Python script that sends a POST request to a URL with an email parameter and displays the response body, using urllib and sys packages.

### 3-error_code.py

A Python script that sends a request to a URL, handles urllib.error.HTTPError exceptions, and displays the HTTP status code if an error occurs.

### 4-hbtn_status.py

A Python script that fetches the status of [https://alx-intranet.hbtn.io] using the requests package and displays the response body.

### 5-hbtn_header.py

A Python script that takes a URL as input, sends a request, and displays the value of the X-Request-Id variable in the response header using the requests and sys packages.

### 6-post_email.py

A Python script that sends a POST request to a URL with an email parameter and displays the response body, using the requests and sys packages.

### 7-error_code.py

A Python script that sends a request to a URL and displays the response body. If the HTTP status code is 400 or greater, it prints the error code.

### 8-json_api.py

A Python script that sends a POST request to a URL with a letter parameter, then parses the JSON response. It displays the id and name if the response is properly formatted and not empty.

### 10-my_github.py

A Python script that uses Basic Authentication with a personal access token to access the GitHub API. It takes GitHub credentials (username and password) and displays the user's id.

### 100-github_commits.py

A Python script that uses the GitHub API to list 10 commits (from most recent to oldest) of a specified repository by a specified user.

## General Requirements

- Scripts should be written in Python 3.8.5.
- Allowed editors include vi, vim, and emacs.
- Scripts should use the pycodestyle for code formatting.
- All files should have executable permissions.
- Each script should have a shebang line at the beginning (`#!/usr/bin/python3`).
- Documentation should be included for all modules, classes, and methods.
- Code should not execute when imported.

## Testing

Scripts can be tested using provided sandbox environments or locally on Ubuntu 20.04 LTS.

## Author

- @waltertaya

## HOWTO Fetch Internet Resources Using `urllib` Package

- `urllib`.request is a Python package/module for fetching URLs.It offers simple interface, in the form of the `urlopen` function. This is capable of fetching URLs using a variety of different protocols. It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on. These are provided by objects called handlers and openers.

```Python
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
```

- If you wish to retrieve a resource via URL and store it in a temporary location, you can do so via the `shutil.copyfileobj()` and `tempfile.NamedTemporaryFile()` functions:
- `shutil.copyfileobj()`
    `shutil.copyfileobj(fsrc, fdst[, length])`
    Copy the contents of the file-like object fsrc to the file-like object fdst. The integer length, if given, is the buffer size. In particular, a negative length value means to copy the data without looping over the source data in chunks; by default the data is read in chunks to avoid uncontrolled memory consumption. Note that if the current file position of the fsrc object is not 0, only the contents from the current file position to the end of the file will be copied.

- `tempfile.NamedTemporaryFile()`
    tempfile.NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None, delete_on_close=True). This function operates exactly as TemporaryFile() does, except the following differences:

    1. This function returns a file that is guaranteed to have a visible name in the file system.
    2. To manage the named file, it extends the parameters of TemporaryFile() with delete and delete_on_close parameters that determine whether and how the named file should be automatically deleted.

    The returned object is always a file-like object whose file attribute is the underlying true file object. This file-like object can be used in a with statement, just like a normal file. The name of the temporary file can be retrieved from the name attribute of the returned file-like object. On Unix, unlike with the TemporaryFile(), the directory entry does not get unlinked immediately after the file creation. If delete is true (the default) and delete_on_close is true (the default), the file is deleted as soon as it is closed. If delete is true and delete_on_close is false, the file is deleted on context manager exit only, or else when the file-like object is finalized. Deletion is not always guaranteed in this case (see object.__del__()). If delete is false, the value of delete_on_close is ignored. Therefore to use the name of the temporary file to reopen the file after closing it, either make sure not to delete the file upon closure (set the delete parameter to be false) or, in case the temporary file is created in a with statement, set the delete_on_close parameter to be false. The latter approach is recommended as it provides assistance in automatic cleaning of the temporary file upon the context manager exit.Opening the temporary file again by its name while it is still open works as follows:

    1. On POSIX (Portable Operating System Interface) the file can always be opened again.

    2. On Windows, make sure that at least one of the following conditions are fulfilled:

        a. delete is false

        b. additional open shares delete access (e.g. by calling os.open() with the flag O_TEMPORARY)

        c. delete is true but delete_on_close is false. Note, that in this case the additional opens that do not share delete access (e.g. created via builtin open()) must be closed before exiting the context manager, else the os.unlink() call on context manager exit will fail with a PermissionError.

    On Windows, if delete_on_close is false, and the file is created in a directory for which the user lacks delete access, then the os.unlink() call on exit of the context manager will fail with a PermissionError. This cannot happen when delete_on_close is true because delete access is requested by the open, which fails immediately if the requested access is not granted.

    On POSIX (only), a process that is terminated abruptly with SIGKILL cannot automatically delete any NamedTemporaryFiles it created.Raises an auditing event tempfile.mkstemp with argument fullpath.Changed in version 3.8: Added errors parameter. Changed in version 3.12: Added delete_on_close parameter.

```Python
import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass
```

- In the case of HTTP, there are two extra things that Request objects allow you to do: First, you can pass data to be sent to the server. Second, you can pass extra information (“metadata”) about the data or about the request itself, to the server - this information is sent as HTTP “headers”. Let’s look at each of these in turn.

## Data

- Sometimes you want to send data to a URL (often the URL will refer to a CGI (Common Gateway Interface) script or other web application). With HTTP, this is often done using what’s known as a POST request. This is often what your browser does when you submit a HTML form that you filled in on the web. Not all POSTs have to come from forms: you can use a POST to transmit arbitrary data to your own application. In the common case of HTML forms, the data needs to be encoded in a standard way, and then passed to the Request object as the data argument. The encoding is done using a function from the urllib.parse library.

```Python
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
```

- If you do not pass the data argument, urllib uses a GET request.

- If you do not pass the data argument, urllib uses a GET request. One way in which GET and POST requests differ is that POST requests often have “side-effects”: they change the state of the system in some way (for example by placing an order with the website for a hundredweight of tinned spam to be delivered to your door). Though the HTTP standard makes it clear that POSTs are intended to always cause side-effects, and GET requests never to cause side-effects, nothing prevents a GET request from having side-effects, nor a POST requests from having no side-effects. Data can also be passed in an HTTP GET request by encoding it in the URL itself. This is done as follows:

```Python
>>> import urllib.request
>>> import urllib.parse
>>> data = {}
>>> data['name'] = 'Somebody Here'
>>> data['location'] = 'Northampton'
>>> data['language'] = 'Python'
>>> url_values = urllib.parse.urlencode(data)
>>> print(url_values)  # The order may differ from below.  
name=Somebody+Here&language=Python&location=Northampton
>>> url = 'http://www.example.com/example.cgi'
>>> full_url = url + '?' + url_values
>>> data = urllib.request.urlopen(full_url)
```

## Headers

- Some websites dislike being browsed by programs, or send different versions to different browsers. By default urllib identifies itself as Python-urllib/x.y (where x and y are the major and minor version numbers of the Python release, e.g. Python-urllib/2.5), which may confuse the site, or just plain not work. The way a browser identifies itself is through the User-Agent header. When you create a Request object you can pass a dictionary of headers in. The following example makes the same request as above, but identifies itself as a version of Internet Explorer.

```Python
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
```

## URLError

- Often, URLError is raised because there is no network connection (no route to the specified server), or the specified server doesn’t exist. In this case, the exception raised will have a ‘reason’ attribute, which is a tuple containing an error code and a text error message.

```Python
>>> req = urllib.request.Request('http://www.pretend_server.org')
>>> try: urllib.request.urlopen(req)
... except urllib.error.URLError as e:
...     print(e.reason)      
...
(4, 'getaddrinfo failed')
```

## info and geturl

- The response returned by urlopen (or the HTTPError instance) has two useful methods info() and geturl() and is defined in the module urllib.response.

    1. geturl - this returns the real URL of the page fetched. This is useful because urlopen (or the opener object used) may have followed a redirect. The URL of the page fetched may not be the same as the URL requested.

    2. info - this returns a dictionary-like object that describes the page fetched, particularly the headers sent by the server. It is currently an http.client.HTTPMessage instance.
- Typical headers include ‘Content-length’, ‘Content-type’, and so on. See the Quick Reference to HTTP Headers for a useful listing of HTTP headers with brief explanations of their meaning and use.
