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
        self.dic[other.name] = other.tid

    def __str__(self):
        lis = []
        for k in sorted(self.dic):
            lis.append('Name: {}'.format(k))
            lis.append('ID: {}'.format(self.dic[k]))
        return '\n'.join(lis)

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()
