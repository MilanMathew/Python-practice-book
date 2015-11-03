#modified unnique function to take an optional
#key function as argument 

def unique(l, key=lambda x: x[0]):
    c = []
    for a in l:
        if key(a) not in c:
            c.append(key(a))
    return c
print(unique(['Python', "python", 'PYTHON', 'java', "Java"], key=lambda s: s.upper()))
