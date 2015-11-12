# prints the external IP 
# address of your machine.
# uses the response from httpbin.org/get
import urllib
import json

data = urllib.urlopen('http://httpbin.org/get')
response = data.read()
print json.loads(response)['origin']
