import sys

def sorter(t):
    return t[-1]

def main():
    dic = {}
    with open(sys.argv[1]) as fd:
        for lines in fd:
            tokens = lines.strip().rsplit(maxsplit=1)
            food, cals = tokens[0], int(tokens[1])
            dic[food] = cals
    person = {}
    for lines in sys.stdin:
        line = lines.strip().split(",")
        name, foods = line[0], line[1:]
        person[name] = 0
        for food in foods:
            if food in dic:
                person[name] += dic[food]
            else:
                person[name] += 100
    key_width = len(max(person.keys(), key=len))
    value_width = len(str(max(person.values())))
    for k, v in sorted(person.items(), key=sorter):
        print("{:>{:d}s} : {:{:d}d}".format(k, key_width, v, value_width))

if __name__ == "__main__":
    main()
