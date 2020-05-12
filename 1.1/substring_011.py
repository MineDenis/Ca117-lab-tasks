import sys

def sub(s):
    return s.lower()

def main():
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].split()
        ok = sub(line[0])
        nice = sub(line[1])
        if ok in nice:
            print("True")
        else:
            print("False")
        i += 1
if __name__ == '__main__':
    main()
