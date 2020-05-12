class Triathlete(object):

    def __init__(self, name, tid, cycle=0, run=0, swim=0):
        self.name = name
        self.tid = tid
        self.swim = swim
        self.run = run
        self.cycle = cycle

    def add_time(self, thing, time):
        if thing == 'swim':
            self.swim += time
        elif thing == 'cycle':
            self.cycle += time
        elif thing == 'run':
            self.run += time

    def get_time(self, thing):
        if thing == 'swim':
            return self.swim
        elif thing == 'cycle':
            return self.cycle
        elif thing == 'run':
            return self.run

    def __eq__(self, other):
        return self.swim + self.cycle + self.run == other.swim + other.cycle + other.run

    def __gt__(self, other):
        return self.swim + self.cycle + self.run > other.swim + other.cycle + other.run

    def __str__(self):
        return 'Name: {}\nID: {}\nRace time: {}'.format(self.name, self.tid, self.cycle + self.swim + self.run)

class Triathlon(Triathlete):
    def __init__(self, dic={}):
        self.dic = {}

    def add(self, other):
        self.dic[other.name] = (other.swim + other.cycle + other.run, other.tid)

    def best(self):
        best = sorted(self.dic.values(), key=min, reverse=True)
        for k, v in self.dic.items():
            if v == best[0]:
                return 'Name: {}\nID: {}\nRace time: {}'.format(k, self.dic[k][1], self.dic[k][0])

    def worst(self):
        worst = sorted(self.dic.values(), reverse=True)
        for k, v in self.dic.items():
            if v == worst[0]:
                return 'Name: {}\nID: {}\nRace time: {}'.format(k, self.dic[k][1], self.dic[k][0])

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()
