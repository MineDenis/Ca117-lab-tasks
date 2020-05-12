class Score:
    def __init__(self, goal=0, point=0):
        self.goal = goal
        self.point = point

    def greater_than(self, point):
        return 3 * self.goal + self.point > point.point + 3 * point.goal

    def less_than(self, point):
        return 3 * self.goal + self.point < point.point + 3 * point.goal

    def equal_to(self, point):
        return 3 * self.goal + self.point == point.point + 3 * point.goal
def main():

    score1 = Score()
    score2 = Score(3, 9)
    score3 = Score(4, 6)

    print(score1.less_than(score2))
    print(score3.less_than(score1))
    print(score1.greater_than(score2))
    print(score3.greater_than(score2))
    print(score1.greater_than(score1))
    print(score2.greater_than(score1))
    print(score2.equal_to(score1))
    print(score3.equal_to(score2))
if __name__ == '__main__':
    main()
