def dups(s):
    c = []
    f = []
    for b in s:
        if b not in c: c.append(b)
        else: f.append(b)
    return f

#def dups(a):
#    f = []
#    d = unique(a)
#    print d
#    for b in a:
"""        if b in d: f.append(b)
    print f
"""

print(dups([1,2,1,3,2,5]))
