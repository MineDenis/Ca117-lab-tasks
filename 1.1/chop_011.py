import sys

def chop(s):
    return s[1:len(s) - 1]

def main():
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        chopped = chop(line)
        if len(chopped) > 0:
            print(chopped)
        i += 1

if __name__ == '__main__':
    main()
