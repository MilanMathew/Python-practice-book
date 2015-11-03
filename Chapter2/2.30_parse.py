import sys
def parse_csv(f):
    fp = open(f, 'r')
    a = fp.read()
    d = a.split('\n')
    d.pop()
    return [x.split(',') for x in d]
print(parse_csv('a.csv'))
