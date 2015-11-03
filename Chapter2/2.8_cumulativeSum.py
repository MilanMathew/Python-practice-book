def cumulative_sum(a):
    result = 0
    c = []
    for b in a:
        result += b
        c.append(result)
    print c

cumulative_sum([1, 2, 3, 4, 5])
#cumulative_sum(['apple', 'is', 'good', 'for', 'health'])
