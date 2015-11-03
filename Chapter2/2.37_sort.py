def valuesort(d):
    return [x[1] for x in sorted(d.items(), key=lambda x: x[0])]

print valuesort({'x':1, 'y':2, 'a':3})
