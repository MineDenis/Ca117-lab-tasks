import sys

def sorter(t):
    return t[-1]

dic = {}
for lines in sys.stdin:
    line = lines.strip().split()
    score = line[-1]
    score = score.split(',')
    total = 0
    for l in score:
        if l == 'X':
            total += 0
        else:
            total += int(l)
    score = total / 6
    name = line[:-1]
    name = ' '.join(name)
    dic[name] = score
for k, v in sorted(dic.items(), key=sorter, reverse=True):
    print('{} {:.1f}'.format(k, v))
