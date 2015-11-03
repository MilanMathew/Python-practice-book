import sys
def center(f):
    fp = open(f, 'r')
    max_length = 0
    result = ''
    fr = fp.readlines()
    for i in range(len(fr)):
        fr[i]  = fr[i].strip()
    for line in fr:
        if max_length < len(line):
            max_length = len(line)
            biggest_line = line
    for line in fr:
        if line == biggest_line:
            result += line + '\n'
        else:
            result = result + addPadding(max_length, len(line)) + line + addPadding(max_length, len(line)) + '\n'
    fp.close()
    return result

def addPadding(maximum, line_length):
    result = ''
    for i in range((maximum - line_length) / 2):
        result = result + ' '
    return result

print center(sys.argv[1])
