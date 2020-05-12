import sys

def main():
    with open(sys.argv[1]) as fd:
        p = fd.readlines()
    line = []
    for lines in sys.stdin:
        line.append(lines)
    print(line)
    for i in range(len(p)):
        for j in range(len(line)):
            censor = "@" * len(p[i].strip())
            if p[i].strip() in line[j]:
                line[j] = line[j].replace(p[i].strip(), censor)
    print("".join(line).rstrip())
if __name__ == "__main__":
    main()
