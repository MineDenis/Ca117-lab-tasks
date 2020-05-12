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

    def __str__(self):
        return 'Name: {}\nID: {}\nRace time: {}'.format(self.name, self.tid, self.cycle + self.swim + self.run)

def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()
