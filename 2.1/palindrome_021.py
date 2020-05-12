import sys

def main():
    for element in sys.stdin:
        element = element.strip()
        for char in element:
            if not char.isalnum():
                element = element.replace(char, "", 1)
        element = element.lower()
        if element == element[::-1]:
            print(True)
        else:
            print(False)

if __name__ == '__main__':
    main()
