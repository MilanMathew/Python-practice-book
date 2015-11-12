# Implements the functionality of python's pydoc.

import sys
import inspect

print 'Help on module ' + sys.argv[1] + ' :'
print '\nDESCRIPTION\n'
print sys.argv[1], '-', __import__(sys.argv[1]).__doc__
print 'FUNCTIONS\n'
for i in inspect.getmembers(sys.argv[1]):
    #print __import__(sys.argv[1]).i.__doc__
    #print i[0].__doc__
    print i[0], type(i[0])
    if inspect.isfunction(i[0]):
        print i[0], '()'
        print i[0].__doc__
