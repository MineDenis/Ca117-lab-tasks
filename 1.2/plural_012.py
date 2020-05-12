import sys

def plural(s):
    vowel = ["i", "o", "u", "e", "a"]
    pog = s[len(s) - 2: len(s)]
    po = s[- 1]
    if pog == "ch" or pog == "sh":
        s = s + "es"
    elif po == "x" or po == "s" or po == "z":
        s = s + "es"
    elif s[-2] not in vowel and s[-1] == "y":
        s = s[:- 1] + "ies"
        pass
    elif po == "f":
        s = s[:- 1] + "ves"
    elif pog == "fe":
        s = s[:len(s) - 2] + "ves"
    elif s[-1] == "o":
        s = s + "es"
    else:
        s = s + "s"
    return s

def main():
    for line in sys.stdin:
        print(plural(line.strip()))

if __name__ == '__main__':
    main()
