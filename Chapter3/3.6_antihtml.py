# download webpage corresponding to the given url and
# print it after stripping off the html tags.
import re
import os
import urllib
import sys

def execute():
    url = sys.argv[1]
    if url.endswith('/'):
        basename='index.html'
    else:
        basename = url.split('/')[-1]
    print 'Saving', url, 'as', basename + '.'
    urllib.urlretrieve(url, os.getcwd() + '/' + basename)
    fp = open(basename, 'r')
    data = re.sub(r'<.*?>', '', fp.read()) 
    return data.strip()          # remove trailing blank lines for aesthetics.

print execute()
