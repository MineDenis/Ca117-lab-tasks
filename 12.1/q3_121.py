import sys

for lines in sys.stdin:
    line = lines.strip()
    lis = [c for c in line.lower() if c in 'aeiou']
    if lis == list('aeiou'):
        print(line)
