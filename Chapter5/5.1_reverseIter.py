# iterator class that takes a list
# iterates it from the reverse direction.


class reverse_iter:
    def __init__(self, l):
        self.l = l

    def next(self):
        try:
            return self.l.pop()
        except IndexError:
            raise StopIteration()
