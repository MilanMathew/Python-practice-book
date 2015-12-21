# Takes an integer n & filename as command line arguments and
# splits the file into multiple small files each having n lines.

import sys
n = int(sys.argv[1])
lines = open(sys.argv[2]).readlines()
length = len(lines)
file_id = 0


def main(lines, file_id):
    if len(lines) != 0:
        filename = '%d.txt' % file_id
        f = open(filename, 'w')
        if length % n == 0:
            for i in range(n):
                f.write(lines[i])
            for file_objects in main(lines[n:], file_id+1):
                yield file_objects
        elif length < n or length % n != 0:
            print "Please retry with another value of n."


files = main(lines, file_id)
for f in files:
    pass
print "The files have been generated!!." 
