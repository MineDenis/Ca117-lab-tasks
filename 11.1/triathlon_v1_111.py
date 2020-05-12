class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return 'Name: {}\nID: {}'.format(self.name, self.tid)

class Triathlon(Triathlete):
    def __init__(self, dic={}):
        self.dic = {}

    def add(self, other):
        self.dic[other.tid] = Triathlete(other.name, other.tid)

    def remove(self, tid):
        del self.dic[tid]

    def lookup(self, tid):
        if tid in dict.keys(self.dic):
            return self.dic[tid]

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)

    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)

if __name__ == '__main__':
    main()
