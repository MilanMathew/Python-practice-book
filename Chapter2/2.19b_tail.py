#the unix command tail
import sys
def tail(f):
    fp = open(f, 'r')
    fl = fp.readlines()
    for x in fl[len(fl)-10:]:
        print x.strip()
    return fp.close()

tail(sys.argv[1])
