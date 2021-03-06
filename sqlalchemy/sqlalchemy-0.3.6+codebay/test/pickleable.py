"""since the cPickle module as of py2.4 uses erroneous relative imports, define the various
picklable classes here so we can test PickleType stuff without issue."""


class Foo(object):
    def __init__(self, moredata):
        self.data = 'im data'
        self.stuff = 'im stuff'
        self.moredata = moredata
    def __eq__(self, other):
        return other.data == self.data and other.stuff == self.stuff and other.moredata==self.moredata


class Bar(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return other.__class__ is self.__class__ and other.x==self.x and other.y==self.y
    def __str__(self):
        return "Bar(%d, %d)" % (self.x, self.y)

class BarWithoutCompare(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Bar(%d, %d)" % (self.x, self.y)
    