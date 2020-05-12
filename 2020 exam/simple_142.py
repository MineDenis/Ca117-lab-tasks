import sys
import math
import re

def main():
    for lines in sys.stdin:
        sett = set()
        counter = 0
        line = lines.strip()
        for char in line:
            if char not in sett:
                sett.add(char)
                counter += 1
        if counter < 2:
            print(0)
        else:
            print(counter - 2)
if __name__ == '__main__':
    main()
