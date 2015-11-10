# parse comma separated values
# from a file.
def parse_csv(f):
    fp = open(f, 'r')
    a = fp.readlines()
    print [x[:-1].split(',') for x in a]
    return fp.close()
parse_csv('a.csv')
