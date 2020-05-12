import sys

def main():
    s = sys.argv[1]
    string = list(s)
    for i in range(1, len(string), 2):
        string[i - 1], string[i] = string[i], string[i - 1]
    print(''.join(string))
if __name__ == '__main__':
    main()
