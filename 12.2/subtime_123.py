import sys
import datetime

def hours(s):
    if s // 60 == -1:
        return '23'
    elif s // 60 == 24:
        return '00'
    elif s // 60 == 0:
        return '00'
    else:
        return s // 60

def mins(s):
    if s % 60 == 0:
        return '00'
    elif len(str(s % 60)) == 1:
        return '0' + str(s % 60)
    else:
        return s % 60

for lines in sys.stdin:
    line = lines.strip().split()
    time, sub = line[0], line[1]
    hour, min = time[0: 2], time[3:]
    time = int(hour) * 60 + int(min)
    if sub[0] != "-":
        new = time - int(sub)
    else:
        new = time + int(sub[1:])
    print('{}:{}'.format(hours(new), mins(new)))
