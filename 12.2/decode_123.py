import sys

vowels = "aeiou"
for lines in sys.stdin:
    line = lines.strip()
    newword = []
    i = 0
    while i < len(line):
        newword.append(line[i])
        i += 3 if line[i] in vowels else 1
    print(''.join(newword))
