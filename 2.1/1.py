import sys, collections

def main():
    lines = sys.stdin.readlines()
    line = lines.split()
    i = 0
    j = 0
    l = []
    while j < len(line[0]):
        l.append(line[0][j])
        j += 1
    p = []
    while i < len(line[1]):
        p.append(line[1][i])
        i += 1
    print(compare([l], [p]))

if __name__ == '__main__':
    main()
