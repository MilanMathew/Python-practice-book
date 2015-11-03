def group(l,n):
    rv = []
    c = 0
    for i in range(1, len(l)/n+1):
        rv.append(l[c:n*i])
        c = n*i
    rv.append(l[c:])
    return rv

print [1,2,3,4,5,6,7,8,9,10,11]
print group([1,2,3,4,5,6,7,8,9,10,11], 3)
