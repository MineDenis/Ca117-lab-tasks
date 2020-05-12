import sys

sett = set()
thing = '!,.'
for lines in sys.stdin:
    line = lines.strip().split()
    newline = []
    for i in range(len(line)):
        if line[i].strip(thing).lower() in sett:
            newline.append(".")
        else:
            newline.append(line[i])
            sett.add(line[i].strip(thing).lower())
    print(' '.join(newline))
