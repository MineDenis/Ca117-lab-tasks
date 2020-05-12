import sys

def rus(s):
    p = 0
    for i in range(len(s)):
        if s.isdigit():
          s[i] =  s[i][:-1]
    print
    return s[: p]

def main():
    global dog
    for line in sys.stdin:
        pog = line.split("@")
        dog = pog[0].split(".")
        dog[1] = rus(dog[1])
        cod = jog(dog)
        print((" ").join(dog))
def jog(s):
    for i in range(len(dog)):
        dog[i] = dog[i].capitalize()
    return " ".join(dog)
if __name__ == '__main__':
    main()
