import sys

def bin(s):
    i = 0
    while i < len(line):
        line[i] = line[i][0: len(line[i]) - 1] + line[i][int(len(line[i]) - 1)].capitalize()
        i += 1
    return " ".join(line)
def main():
    global line
    for line in sys.stdin:
        line = line.strip().split()
        camel = bin(line)
        print(camel)

if __name__ == '__main__':
    main()
