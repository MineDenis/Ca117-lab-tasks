class Patient(object):

    def __init__(self, name, age, doctor):
        self.name = name
        self.age = age
        self.doctor = doctor

    def __str__(self):
        return "Name: {}\nAge: {}\nDoctor: {}".format(self.name, self.age, self.doctor)

class Ward(object):

    def __init__(self):
        self.d = {}

    def add(self, element):
        self.d[element.name] = element

    def remove(self, name):
        del self.d[name]

    def lookup(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None

def main():
    p1 = Patient('Mary', 34, 'James Kildare')
    p2 = Patient('Wendy', 40, 'Gregory House')

    w = Ward()

    w.add(p1)
    w.add(p2)

    p = w.lookup('Mary')
    assert(isinstance(p, Patient))
    assert(p.name == 'Mary')
    assert(p.age == 34)

    w.remove('Mary')
    p = w.lookup('Mary')
    assert(p is None)

if __name__ == '__main__':
    main()
