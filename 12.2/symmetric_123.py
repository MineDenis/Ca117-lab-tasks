import sys

lis = [line.strip() for line in sys.stdin]

if len(lis) % 2 == 1:
    for i in range(0, len(lis), 2):
        print(lis[i])
    for i in range(1, len(lis), 2):
        print(lis[::-1][i])
else:
    for i in range(0, len(lis), 2):
        print(lis[i])
    for i in range(0, len(lis), 2):
        print(lis[::-1][i])
