#prints words in the descending
#order of their occurences in a file.
def word_frequency(wordlist):
    worddict = {}
    for word in wordlist:
        worddict[word] = worddict.get(word, 0) + 1
    return worddict

def read_words(filename):
    return open(filename).read().split()

def main(filename):
    frequency = word_frequency(read_words(filename))
    result = []
    for word, count in frequency.items():
        result.append((word, count))
    result = sorted(result, key=lambda x: x[1])

    for i in range(len(result)-1, 0, -1): 
        print result[i][0], result[i][1]
    
if __name__ == "__main__":
    import sys
    print(main(sys.argv[1]))
