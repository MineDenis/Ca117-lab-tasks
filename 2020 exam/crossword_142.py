import sys
import math
import re

def crossword(word1, word2):
    for across in range(len(word1)):
        for down in range(len(word2)):
            if word2[down] == word1[across]:
               return across, down
def main():
    for lines in sys.stdin:
        word1, word2 = lines.strip().split()
        x = 0
        y = 0
        x, y = crossword(word1, word2)
        for i in range(0, len(word2)):
            if i == x:
                print(word1)
            else:
                print(x * "." + word2[i] + (int(len(word1) - (x + 1)) * "."))

if __name__ == '__main__':
    main()
