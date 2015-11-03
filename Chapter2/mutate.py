#deletion complete
#swapping complete
#replacing complete
#insertion complete
def mutate(s):
    import string
    lowercase = string.lowercase
    l = []
    for i in range(len(s)):             # single deletions.
        l.append(s[:i] + s[i+1:])

    for i in range(len(s)-1):           # swapping consecutive chars.
        l.append(s[:i] + s[i+1] + s[i] + s[i+2:])

    for i in range(len(s)):             # replacing single char.
        for j in lowercase:
            l.append(s[:i] + j + s[i+1:])

    for i in lowercase:
        for j in range(len(s) + 1):
            l.append(insert(s, j, i))

    return l

def insert(s, index, char):             # insert char at index of s.
    return s[:index] + char + s[index:]

print(mutate('python'))
