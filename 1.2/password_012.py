import sys

def dog(s):
    ok = 0
    okk = 0
    nice = 0
    pog = 0
    for element in s:
        if element.isdigit():
            ok = 1
        elif element.isupper():
            okk = 1
        elif element.islower():
            nice = 1
        else:
            pog = 1
    return pog + nice + okk + ok

def main():
    for line in sys.stdin:
        print(dog(line.strip()))

if __name__ == '__main__':
    main()
