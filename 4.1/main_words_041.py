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
    maxl = 0
    maxw = 0
    for (k, v) in sorted(d.items()):
        if len(str(v)) > maxl:
            maxl = len(str(v))
    for (k, v) in sorted(d.items()):
        if len(k) >= 4 and v >= 3:
            if len(k) > maxw:
                maxw = len(str(k))
    for (k, v) in sorted(d.items()):
        if len(k) >= 4 and v >= 3:
            print('{:>{}s} : {:>{}d}'.format(k, maxw, v, maxl))
if __name__ == '__main__':
    main()
