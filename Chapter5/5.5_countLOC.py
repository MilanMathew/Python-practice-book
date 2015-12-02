# Function computes the total number of lines of code (LOC) 
# in all py files in a specified directory recursively.

import os
import sys

count = 0


def main(direc):
    files = os.listdir(direc)
    global count
    for f in files:
        location = os.path.abspath(direc + '/' + f)
        if os.path.isdir(location):
            for i in main(location):
                yield i
        else:
            if f[-3:] == '.py':
                for line in open(f):
                    count += 1

a = main(sys.argv[1])
for i in a:                      # this step is necessary so that
    pass                         # one iteration is completed.
print count
