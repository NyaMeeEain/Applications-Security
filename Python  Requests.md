### Python Requests Modules
```
import urllib
import urllib2
target = 'http://vic/login.php'

req = urllib2.Request(url = target)
values = {'param1' : 'value1', 'param2' : 'value2','param3' : 'value3'}
req.add_data(urllib.urlencode(values))
response = urllib2.urlopen(req)
body = response.read()
```

### Python POST with COOKIE
```
import urllib
import urllib2
cookie='VALUE'

url = 'http://vic/index.php'
referrer = 'http://vic/referrer.php'

values = {'param1' : 'value1',
          'param2' : 'value2',
          'param3' : 'value3',
          'param4' : 'value4' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
req.add_header('Cookie', cookie)
req.add_header('Referrer', referrer)
try:
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page
except HTTPError, e:
    print e.reason

```
### Python function to time a GET Request
```
def check_char():
    url = 'https://ip/vuln.php'
    start=time.time()
    urllib.urlopen(url)
    end =time.time()
    howlong=end-start
    return howlong

```
