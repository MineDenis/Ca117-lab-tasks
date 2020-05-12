import sys

def main():
    for lines in sys.stdin:
        line = lines.strip()
        l = [c for c in line.lower() if c in "aeiou"]
        if l == list('aeiou'):
            print(line)

if __name__ == "__main__":
    main()
