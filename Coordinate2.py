class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other):
        assert type(other) == type(self)
        return self.x == other.x and self.y == other.y
        
    def __repr__(self):
        return "Coordinate(%i, %i)" % (self.getX(), self.getY())


a = Coordinate(2, 3)
b = Coordinate(2, 4)

print a==b
print a
print repr(a)