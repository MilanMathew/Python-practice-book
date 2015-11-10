import os
import sys
dir=sys.argv[1]
print dir
def dirtree(dir,i):
    filenames=os.listdir(dir)
    a='|--'
    b='|   '
    c = '\--'
    filenames.sort()
    for filename in filenames:
        if not os.path.isdir(os.path.abspath(dir+'/'+filename)):
            #print os.path.abspath(filename)
            if filename==filenames[-1]:	
                print b*i+c,filename
            else:
                print b*i+a,filename
        else:
            print b*i+a,filename
            dir=dir+'/'+filename
            dirtree(dir,i+1)

dirtree(dir,i=0)
