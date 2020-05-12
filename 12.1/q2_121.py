import sys

lis = []
for lines in sys.stdin:
    line = lines.strip().split()
    lis.append(line)
answer = []
for i in range(len(lis[0])):
    if lis[0][i] == lis[1][i]:
        answer.append(i)
print(answer)
