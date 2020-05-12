import sys

word, num = sys.argv[1], int(sys.argv[2])
for i in range(num):
    word = word[1:] + word[0]
print(word)
