#interchanges keys and values in a dict.
def invertdict(D):
    result = {}
    for i in D.iteritems():
        result[i[1]] = i[0]
    return result

print invertdict({'x': 1, 'y': 2, 'z': 3})
