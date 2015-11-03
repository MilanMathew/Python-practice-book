def lensort(l):
    l.sort(key=lambda x: len(x))
    return l


print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
