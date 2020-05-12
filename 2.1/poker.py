import sys

if __name__ == '__main__':
    s = int(sys.argv[1])
    m = (s * 2) -1
    for i in range(int(s / 2)):
        print("{:{}}").format("* ")
    
