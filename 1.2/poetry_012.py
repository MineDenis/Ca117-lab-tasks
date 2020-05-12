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
    maxl = len(p)
    i = 0
    while i < len(lines):
        print('{:^{}s}'.format(lines[i].strip(), maxl))
        i += 1

if __name__ == '__main__':
    main()
