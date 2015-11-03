import sys
def wrap(f, w):
    fp = open(f, 'r')
    spos = 1
    fr = fp.readlines()

    result = ''
    for i in range(len(fr)):
        for s in fr[i]:
            result = result + s 
            if spos % (int(w)) == 0:
                result = result + '\n'
            spos += 1
        spos = 1
    fp.close()
    return result

print(wrap(sys.argv[1], sys.argv[2]))
