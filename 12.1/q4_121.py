import sys
import re

for lines in sys.stdin:
    line = lines.strip()
    line = re.findall('[A-Z][^A-Z]*', line)
    lis = []
    lis.append(line[0])
    for i in range(1, len(line)):
        lis.append(line[i].lower())
    print(' '.join(lis))
