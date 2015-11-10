import re
def make_slug(name):
    array = re.findall('\w+',name)
    array = '-'.join(array)
    return array 

print make_slug("hello world")
print make_slug("hello  world!")
print make_slug(" --hello- world--")
