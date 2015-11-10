#find anagrams in a list.

def anagrams(L):
    output, keys, result = {}, [], []
    for word in L:
        sortedWord = ''.join(sorted(word))  #group together words having same chars.
        output.setdefault(sortedWord, []).append(word)
    for entry in output:
        keys.append(entry)
    keys.sort()
    for entry in keys:
        result.append(output[entry])
    return result

print anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
