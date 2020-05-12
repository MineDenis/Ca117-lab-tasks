class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        midx = (self.x + other.x) / 2
        midy = (self.y + other.y) / 2
        return Point(midx, midy)

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)

class Circle(object):
    def __init__(self, p1, radius):
        self.p1 = p1
        self.radius = radius

    def __add__(self, other):
        self.p1 = self.p1.midpoint(other.p1)
        self.radius = self.radius + other.radius
        return self

    def __str__(self):
        return 'Centre: {}\nRadius: {}'.format(self.p1, self.radius)
