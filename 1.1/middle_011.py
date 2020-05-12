import sys

def mid(s):
    mid = int(len(s) / 2)
    return s[mid]

def main():
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        middle = mid(line)
        if len(line) % 2 != 0:
            print(middle)
        else:
            print("No middle character!")
        i += 1
if __name__ == '__main__':
    main()
