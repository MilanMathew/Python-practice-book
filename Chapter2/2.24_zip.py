def zip(l1, l2):
    return [(l1[x], l2[x]) for x in range(len(l1))]

print (zip([1,2,3], ['a', 'b', 'c']))
