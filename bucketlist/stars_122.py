import sys

def main():
    stars = []
    for lines in sys.stdin:
        line = lines.strip().split()
        stars.append(line)
    
    lines = int(stars[0][0])
    lent = int(stars[0][1])
    del stars[0]
    count = 0
    dict = {}
    for line in stars:
        points = []
        for i in line:
            for j in range(1, lent):
                if i[j] == "-":
                    points.append(j)
        dict[count] = points
        count += 1
    count = 0
    seen = dict[0]
    final = 0
    for i in range(1, len(dict)):
        good_value = []
        for j in range(len(dict[i]) - 1):
            if dict[i][j] not in seen:
                seen.append(dict[i][j])
                good_value.append(dict[i][j])
            elif dict[i][j] in seen:
                good_value.append(dict[i][j])
            for p in range(len(seen)):
                print(seen[0])
                if int(seen[p]) not in good_value and int(seen[p]) - 1 not in good_value and int(seen[p]) + 1 not in good_value:
                    final += 1
                    del seen[p]
            
    print(final)

if __name__ == '__main__':
    main()
