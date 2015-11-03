def enumerate(l):
    return [(x, l[x]) for x in range(len(l))]

print (enumerate(['a', 'b', 'c']))
for index, value in enumerate(['a', 'b', 'c']):
    print index, value
