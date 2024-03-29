## 🚀 Project Descriptions

### 📋 **0-hbtn_status.py**

```python
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io') as response:
   html = response.read()
   ```
## 📜 1-hbtn_header.py
```python
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(response.headers.get('X-Request-Id'))
```
## 📧 2-post_email.py
```python
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
values = {'email': 'example@example.com'}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
```
## 🛑 3-error_code.py
```python
import urllib.request
import urllib.error
import sys

url = sys.argv[1]
try:
    with urllib.request.urlopen
```
