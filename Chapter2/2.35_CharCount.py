#counts the character frequency in a file.

import sys
def main(filename):
    freq = {}
    result = []
    fp = open(filename, 'r')
    for c in fp.read():
        if c!= '\n':
            freq[c] = freq.get(c, 0) + 1
    for i, j in freq.iteritems():
         result.append((i, j))
    result.sort(key=lambda x: x[1], reverse=True)
    for i, j in result:
        print i, j
    return fp.close()

if __name__ == '__main__':
    main(sys.argv[1])
