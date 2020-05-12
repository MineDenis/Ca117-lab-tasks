import sys

def main():
    d = {}
    f = sys.argv[1]
    with open(f) as fd:
        con = fd.readlines()
    for i in range(len(con)):
        con[i] = con[i].strip().split(" ")
        d[con[i][0]] = con[i][1], con[i][2]
    for line in sys.stdin:
        line = line.strip()
        if line in d:
            print("Name: {}".format(line))
            print("Phone: {}".format(d[line][0]))
            print("Email: {}".format(d[line][1]))
        else:
            print("Name: {}".format(line))
            print("No such contact")
if __name__ == '__main__':
    main()
