def min(a):
    result = a[0]
    for b in a:
        if (b < result): result = b
    print result

def max(a):
    result = a[0]
    for b in a:
        if (b > result): result = b
    print result

min([1,2,3,4,5])
max([1,2,3,4,5])

min(['apple', 'ball', 'cat'])
max(['apple', 'ball', 'cat'])
