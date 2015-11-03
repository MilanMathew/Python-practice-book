import sys

def reverse(f):
    for i in (open(f).read().split('\n')[::-1]):
        print i

reverse(sys.argv[1])
