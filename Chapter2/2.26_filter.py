def even(a): return a%2 == 0
f = even
l = [1, 2, 3, 4, 5, 6]
print([x for x in l if f(x)])
