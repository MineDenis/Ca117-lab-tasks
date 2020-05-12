import sys

def sorter(t):
    return t[-1]

def main():
    exam = {}
    skipped = []
    for lines in sys.stdin:
        line = lines.strip().split(":")
        name, numbers = line[0], line[1].split(",")
        total = 0
        try:
            for num in numbers:
                total += int(num)
        except ValueError:
                skipped.append(name)
        else:
            exam[name] = total
    for k, v in sorted(exam.items(), key=sorter, reverse=True):
        print("{:s} : {:d}".format(k, v))
    print("Skipped:")
    for i in range(len(skipped)):
        print(skipped[i])

if __name__ == "__main__":
    main()
