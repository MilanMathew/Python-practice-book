import os, sys
def count(p):
    freq  ={}
    w = os.listdir(p).sort(key=lambda x: x.split('.')[1])
    print(w)
   # for item in os.listdir(p):
   #     print       #  print item

print (count(sys.argv[1]))
