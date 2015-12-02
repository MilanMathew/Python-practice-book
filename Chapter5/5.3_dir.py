# Function recursively descends the directory tree for the specified directory
# and generates paths of all the files in the tree.

import os
import sys


def findfiles(direc):
    files = os.listdir(direc)
    for f in files:
        location = os.path.abspath(direc + '/' + f)
        if not os.path.isdir(location):
            yield location
        else:
            for i in findfiles(location):
                yield i
a = findfiles(sys.argv[1])
for i in a:
    print i
