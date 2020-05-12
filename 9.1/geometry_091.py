from math import sqrt

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Shape(object):
    def __init__(self, points):
        self.points = points

    def sides(self):
        all = []
        for i in range(len(self.points) - 1):
            all.append(Point.distance(self.points[i], self.points[i + 1]))
        all.append(Point.distance(self.points[len(self.points) - 1], self.points[0]))
        return all

    def perimeter(self):
        return sum(self.sides())

class Triangle(Shape):
    def area(self):
        shape_sides = self.sides()
        s = (shape_sides[0] + shape_sides[1] + shape_sides[2]) / 2
        return sqrt(s * (s - shape_sides[0]) * (s - shape_sides[1]) * (s - shape_sides[2]))

class Square(Shape):
    def area(self):
        return self.sides()[0] ** 2
