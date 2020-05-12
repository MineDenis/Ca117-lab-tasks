import sys

def bin(s):
    v = 0
    i = 0
    total = 0
    while i < len(num):
        lenght = len(num) - i - 1
        if num[i] == "0":
            total = total + 0 * (int(form) ** lenght)
        else:
            total = total + int(num[i]) * (int(form) ** lenght)
        i += 1
    return total
def main():
    global num, form
    for line in sys.stdin:
        line = line.strip().split()
        ok = int(line[1])
        num = line[0]
        form = line[1]
        dec = bin(num)
        print(dec)
if __name__ == '__main__':
    main()
