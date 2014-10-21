class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
        #self.intersection = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def intersect(self, other):
        self.intersection = intSet()
        if self.vals == [] or other.vals == []:
            return self.intersection
        for int in self.vals:
            if int in other.vals:
                self.intersection.vals.append(int)
        return self.intersection 
        
    def __len__(self):
        return len(self.vals)



s = intSet()
#print s
s.insert(3)
s.insert(4)
s.insert(5)
print s
#s.insert(3)
#print s
#s.member(3)
#s.member(5)
#s.insert(6)
#print s
#s.remove(3)
#print s
#s.remove(3)

s2 = intSet()
#s2.insert(4)
#s2.insert(5)
s2.insert(6)
s2.insert(7)
print s2

print s.intersect(s2)
print len(s)
