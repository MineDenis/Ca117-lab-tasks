import sys

def cap(s):
    i = 0
    while i < len(camel):
        camel[i] = camel[i].capitalize()
        i += 1
    return " ".join(camel)
def main():
    global pog
    for line in sys.stdin:
        camel = line.strip().split()
        camelcase = cap(camel)
        print(camelcase)
if __name__ == '__main__':
    main()
