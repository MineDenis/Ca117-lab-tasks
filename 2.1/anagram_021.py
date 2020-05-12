import sys

def anagrams(s):
    s = s.strip().split()
    left = s[0]
    right = s[1]
    for char in left:
        if char in right:
            right = right.replace(char, "", 1)
            left = left.replace(char, "", 1)
    if right == "" and left == "":
        return True
    else:
        return False

def main():
    for line in sys.stdin:
        print (anagrams(line))

if __name__ == '__main__':
    main()
