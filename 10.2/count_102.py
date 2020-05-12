def count_letters(m):
    if m == '':
        return 0
    else:
        return 1 + count_letters(m[1:])

def main():
    len = None
    print(count_letters('cat'))
    print(count_letters('catastrophe'))
    print(count_letters(''))

if __name__ == '__main__':
    main()
