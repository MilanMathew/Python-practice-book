def cumulative_product(a):
    result = 1 
    c = []
    for b in a:
        result *= b
        c.append(result)
    print c


cumulative_product([1, 2, 3])
