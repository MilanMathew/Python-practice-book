#the unix command head
import sys
def head(f):
    fp = open(f, 'r')
    for i in range(10):
        print fp.readline().strip()
    return fp.close()

head(sys.argv[1])
