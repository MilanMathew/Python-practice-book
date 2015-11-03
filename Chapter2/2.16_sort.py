#To sort files based on extension
def extsort(l):
    l.sort(key=lambda x: x.split('.')[1])
    return l

print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
