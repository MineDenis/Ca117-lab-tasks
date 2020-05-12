import sys

def cum(s):
    return s[1]
def main():
    s = sys.stdin.read().lower()
    d = {}
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(5):
        counter = s.count(vowels[i])
        d[vowels[i]] = counter
    maxl = 0
    for (k, v) in sorted(d.items(), key=cum, reverse=True):
        if v > maxl:
            maxl = v
    maxl = len(str(maxl))
    for (k, v) in sorted(d.items(), key=cum, reverse=True):
        print('{} : {:{}d}'.format(k, v, maxl))
if __name__ == '__main__':
    main()
