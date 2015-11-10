#prints filename, length(no.of lines) and 
#last modified date separated by tabs 
#in a directory.
import os, time, sys
for item in os.listdir(sys.argv[1]):
    print item, '\t', sum(1 for line in open(item)), '\t', time.ctime(os.stat(item)[8])
