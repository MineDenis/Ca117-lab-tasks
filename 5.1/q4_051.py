import sys
def median(a):
    sorted_a = sorted(a)
    if len(a) % 2 == 0:
        return sum(sorted_a[(len(a) // 2) - 1: (len(a) // 2) + 1]) / 2
    else:
        return sorted_a[(len(a) - 1) // 2]
def main():
    l = []
    for lines in sys.stdin:
        line = lines.strip()
        l.append(int(line))
    total = 0
    for i in range(len(l)):
        total += int(l[i])
    mid = median(l)

    print("Mean: {:.1f}".format(total / len(l)))
    print("Median: {:.1f}".format(mid))
if __name__ == "__main__":
    main()
