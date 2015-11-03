def reverse(a):
    c = []
    length = len(a)
    for b in a:
        c.append(a[length - 1])
        length -= 1
    print c

reverse([1, 2, 3, 4])
