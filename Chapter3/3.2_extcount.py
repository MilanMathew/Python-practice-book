#prints count of each extension in a directory.
import os, sys
def count(directory):
    freq = {}
    result = []
    for item in os.listdir(directory):
        freq[item[item.find('.')+1:]] = freq.get(item[item.find('.')+1:], 0) + 1 
    for item in freq.items():
         result.append(item)
    result.sort(key=lambda x: x[1])
    for x, y in result[::-1]:
        print y, x

if __name__ == '__main__':
    print count(sys.argv[1])
