import sys

def sub(s):
    return s.lower()

def main():
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].split()
        line1 = sub(line[0])
        line2 = sub(line[1])
        j = []
        counter = 0
        p = 0
        while p < len(line1):
            if line1[p] in line2 and not(line1[p] in j):
                counter += 1
                j.append(lin1[p])
            p += 1
        if counter == len(line1):
            print("True")
        else:
            print("False")
        i += 1
if __name__ == '__main__':
    main()
