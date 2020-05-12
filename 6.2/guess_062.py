from random import randint

z = randint(0, 100000)
def guess(g):
    if g == z:
        return 0
    elif g < z:
        return -1
    else:
        return 1

def find():
    top = 1000000
    bot = 0
    mid = (top + bot) // 2
    guessed = guess(mid)
    while guessed != 0:
        if guessed == -1:
            bot = mid + 1
        else:
            top = mid - 1
        mid = (top + bot) // 2
        guessed = guess(mid)
    return mid

def main():
    a = find()
    if a == z:
        print('Correct!')
    else:
        print('Incorrect!')
    print('You said {:d} and answer is {:d}'.format(a, z))

if __name__ == '__main__':
    main()
