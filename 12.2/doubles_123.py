import sys
import re

high = 0
total = []
for lines in sys.stdin:
    line = lines.strip()
    num = len(re.findall(r'aa|ee|ii|oo|uu', line))
    if num > high:
        new = line
        high = num
print(new)
