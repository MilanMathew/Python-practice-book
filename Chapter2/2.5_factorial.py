def product(l):
    result = 1
    for a in l:
        result *= a
    return result

def factorial(n):
    return product(range(1, n+1))

print factorial(4)
