class Weight(object):

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    def from_ounces(other):
        pounds = other // 16
        ounces = other % 16
        return Weight(pounds, ounces)

    def __str__(self):
        return '{} pound(s) and {} ounce(s)'.format(self.pounds, self.ounces)

    def __gt__(self, other):
        return self.pounds * 16 + self.ounces > other.pounds * 16 + other.ounces

    def __eq__(self, other):
        return self.pounds * 16 + self.ounces == other.pounds * 16 + other.ounces

    def __ge__(self, other):
        return self.pounds * 16 + self.ounces >= other.pounds * 16 + other.ounces

    def __add__(self, other):
        new = self.pounds * 16 + self.ounces + other.pounds * 16 + other.ounces
        new = Weight.from_ounces(new)
        return new

    def __iadd__(self, other):
        self.pounds, self.ounces = self.pounds + other.pounds, self.ounces + other.ounces
        return self

    def __mul__(self, other):
        return Weight.from_ounces((self.pounds * 16 + self.ounces) * other)

def main():

    # Create some weights
    w1 = Weight()
    w2 = Weight(6, 4)
    w3 = Weight.from_ounces(100)

    # Confirm all are instances of Weight
    assert(isinstance(w1, Weight))
    assert(isinstance(w2, Weight))
    assert(isinstance(w3, Weight))

    # Ounces per pound
    print('Ounces in a pound: {}'.format(Weight.OUNCES_PER_POUND))

    # Display weights
    print('Weights...')
    print(w1)
    print(w2)
    print(w3)

    # Check relations
    assert(w1 != w2)
    assert(w2 == w3)
    assert(w1 < w2)
    assert(w3 > w1)
    assert(w2 >= w3)

    # Addition
    print('Addition...')
    w4 = w2 + w3
    assert(isinstance(w4, Weight))
    print(w4)

    # In-place addition
    print('In-place addition...')
    w2_alias = w2
    w2 += w3
    assert(w2 is w2_alias)
    print(w2)

    # Multiplication
    print('Multiplication...')
    w5 = w3 * 3
    assert(isinstance(w5, Weight))
    print(w5)

if __name__ == '__main__':
    main()
