#!/usr/bin/env python3

import sys

def main():
    s = int(sys.argv[1])
    i = 1
    while i < s:
        pog = i * "* "
        print("{:^{}}".format(pog[0: -1], s * 2 - 1).rstrip())
        i += 1

    while i > 0:
        pog = i * "* "
        print("{:^{}}".format(pog[0: -1], s * 2 - 1).rstrip())
        i -= 1

if __name__ == '__main__':
    main()
