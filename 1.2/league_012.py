import sys

def main():
    lines = sys.stdin.readlines()
    i = 1
    line = lines[0].strip()
    p = line
    while i < len(lines):
        lineq = lines[i].strip()
        if len(lineq) > len(line):
            p = lineq
            line = p
        i += 1
    p = p.split()
    i = 1
    while not(p[i].isdigit()):
        i += 1
    L = " ".join(p[1:i])
    lenght = len(L)
    print('{:>3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format("POS", "CLUB", lenght, "P", "W", "D", "L", "GF", "GA", "GD", "PTS"))
    i = 1
    j = 0
    while i < len(lines) + 1:
        p = 1
        line = lines[j].split()
        while not(line[p][0].isdigit()):
            p += 1
        pos = "".join(line[:1])
        club = " ".join(line[1: p])
        h = "".join(line[p])
        w = "".join(line[p + 1])
        d = "".join(line[p + 2])
        l = "".join(line[p + 3])
        gf = "".join(line[p + 4])
        ga = "".join(line[p + 5])
        gd = "".join(line[p + 6])
        pts = "".join(line[p + 7])
        print('{:>3s} {:{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(pos, club, lenght, h, w, d, l, gf, ga, gd, pts))
        i += 1
        j += 1

if __name__ == '__main__':
    main()
