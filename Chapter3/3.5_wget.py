# downloads and saves the webpage
# corresponding to the given url.
import os
import sys
import urllib

url = sys.argv[1]
if url.endswith('/'):
    basename = 'index.html'
else:
    basename = url.split('/')[-1]
print 'Saving', url, 'as', basename + '.'
urllib.urlretrieve(url, os.getcwd()+'/'+basename)
