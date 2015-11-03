#reverses each line of the file.
import sys
def reverseline(f):
    fp = open(f)
    a = fp.read().strip().split('\n')
    for i in a:
        print i[::-1]
    return fp.close()

print reverseline(sys.argv[1])
