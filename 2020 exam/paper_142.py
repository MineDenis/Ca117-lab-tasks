import sys
import math
import re

def main():

    for lines in sys.stdin:
        obj1, obj2 = lines.strip().split()

        if obj1 == 'paper' and obj2 == 'rock':
            print('Player 1 wins')
        elif obj1 == 'rock' and obj2 == 'paper':
            print('Player 2 wins')
        elif obj1 == 'rock' and obj2 == 'scissors':
            print('Player 1 wins')
        elif obj1 == obj2:
            print('Draw')
        elif obj1 == 'paper' and obj2 == 'scissors':
            print('Player 2 wins')
        elif obj1 == 'scissors' and obj2 == 'paper':
            print('Player 1 wins')
        elif obj1 == 'scissors' and obj2 == 'rock':
            print('Player 2 wins')

if __name__ == '__main__':
    main()
