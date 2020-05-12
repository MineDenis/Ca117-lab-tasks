import sys

def transform(c):
    if c.isupper():
        return c
    return "0"
def main():
    for lines in sys.stdin:
        line = lines.strip()
        new_line = "".join([transform(c) for c in line])
        cap_line = new_line.split("0")
        print(max(cap_line, key=len))
if __name__ == "__main__":
    main()
