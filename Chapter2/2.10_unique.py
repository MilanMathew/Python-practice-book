def unique(a):
    c = []
    for b in a:
        if b not in c: c.append(b)
    return c

print(unique([1,2,1,3,2,5]))
