import sys
from math import pi

def mat(s):
    return "{:.{}f}".format(pi, n)

def main():
    global n
    n = sys.argv[1]
    print(mat(n))

if __name__ == '__main__':
    main()
