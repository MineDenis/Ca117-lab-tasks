class Score(object):
    def __init__(self, goal=0, point=0):
        self.goal = goal
        self.point = point

    def __eq__(self, point):
        return 3 * self.goal + self.point == point.point + 3 * point.goal

    def __gt__(self, point):
        return 3 * self.goal + self.point > point.point + 3 * point.goal

    def __ge__(self, point):
        return 3 * self.goal + self.point >= point.point + 3 * point.goal

    def __mul__(self, other):
        return Score(self.goal * other, self.point * other)

    def __rmul__(self, other):
        return Score(self.goal * other, self.point * other)

    def __imul__(self, other):
        self.goal *= other
        self.point *= other
        return self

    def __add__(self, point):
        return Score(self.goal + point.goal, self.point + point.point)

    def __sub__(self, point):
        return Score(self.goal - point.goal, self.point - point.point)

    def __iadd__(self, point):
        self.goal += point.goal
        self.point += point.point
        return self

    def __isub__(self, point):
        self.goal -= point.goal
        self.point -= point.point
        return self

    def __str__(self):
        return "{} goal(s) and {} point(s)".format(self.goal, self.point)
