import sys

string, n = sys.argv[1], sys.argv[2]
for i in range(int(n) % len(string)):
    string = string[-1] + string[:-1]
print(string)
