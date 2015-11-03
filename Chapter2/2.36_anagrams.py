#not perfect!!
def anagrams(wordList):
    anagramList = []
    result = []
    count = 0
    for word1 in range(len(wordList)):
        result = result + [[]]
        for word2 in wordList:
            if isAnagram(wordList[word1], word2):
                result[count].append(word2)
        count += 1
    return filterDuplicates(result)

def isAnagram(word1, word2):
    flag = len(word1)==len(word2)
    if not flag:
        return flag
    for char in word1:
        flag = flag and char in word2
    return flag

def filterDuplicates(L):
    final_result = []
    for anagrams in L:
        if anagrams not in final_result:
            final_result.append(anagrams)
    return final_result

print (anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']))
print (anagrams(['pot', 'top', 'done', 'tea', 'soup', 'node']))
