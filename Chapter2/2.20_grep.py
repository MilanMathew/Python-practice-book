#unix command grep
import sys
def grep(f, s):
    fp = open(f, 'r')
    fl = fp.readlines()
    for i in fl:
        if s in i: print i.strip()
    return fp.close()

grep(sys.argv[1], sys.argv[2])
