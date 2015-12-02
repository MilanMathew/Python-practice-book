# Program takes one or more files as args and
# prints lines which are longer than 40 chars.

import sys


def fileopen(l):
    for f in l:
        for line in open(f):
            yield line


def generate(f):
    return(line for line in f if len(line) > 40)


def printlines(genOb):
    for ob in genOb:
        print ob

a = fileopen(sys.argv[1:])
b = generate(a)
printlines(b)
