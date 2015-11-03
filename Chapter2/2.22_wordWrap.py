#***NOT COMPLETE***


#**NOT COMPLETE**
import sys
def wrap(f, w):
    fp = open(f, 'r')
    spos = 1
    fr = fp.readlines()

    result = ''
    for i in range(len(fr)):
        for word in fr[i].split():
            if word[-1] == '.':
                result = result + word + '\n'
            if 30 - spos < len(word):
                result = result + '\n'
            #else:
            result = result + word + ' '
            if spos % (int(w)) == 0:
                result = result + '\n'
            spos += len(word)
        spos = 1
    fp.close()
    return result

print(wrap(sys.argv[1], sys.argv[2]))
