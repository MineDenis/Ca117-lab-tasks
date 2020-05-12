import sys

def main():
    line = []
    for lines in sys.stdin:
        line.append(lines.strip())
    print('Words with q but no u: {}'.format([i for i in line if i.lower().count('q') > i.lower().count('qu')]))

if __name__ == "__main__":
    main()
