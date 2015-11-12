def enumerate(l):
    """ Emulates the enumerate() function.
    """
    return iter([(x, l[x]) for x in range(len(l))])
    
ans = enumerate(['a', 'b', 'c'])
for i in ans:
    print i
