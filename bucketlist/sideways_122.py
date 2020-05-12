import sys

def main():
    sideways = []
    for lines in sys.stdin:
        line = lines.strip()
        line = [c for c in line]
        sideways.append(line)
    len_d, len_s, vertical = len(sideways), len(sideways[0]), []
    for i in range(len_s):
        new_word = []
        for j in range(len_d):
            new_word.append(sideways[j][i])
        vertical.append("".join(new_word))
    vertical = sorted(vertical, key=str.lower)
    for i in range(len(vertical[0])):
        for x in vertical:
            print(x[i], end="")
        print()
if __name__ == '__main__':
    main()
