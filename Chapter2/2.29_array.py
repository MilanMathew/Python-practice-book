def array(n1, n2):
    return [[[None].append([None]) for x in range(n1)]] + [[[None].append([None]) for y in range(n2)]]

a = array(2,3)

a[0][0] = 5
print a
