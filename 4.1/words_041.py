import sys
from string import punctuation

def main():
    d = {}
    s = sys.stdin.read().lower()
    slist = s.split()
    new = [s.strip(punctuation) for s in slist]
    for i in range(len(slist)):
        counter = new.count(new[i])
        d[new[i]] = counter
    for (k, v) in sorted(d.items()):
        print('{} : {}'.format(k, v))
if __name__ == '__main__':
    main()
