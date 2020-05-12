from stack_092 import Stack
import sys

def matcher(line):
    if len(line) % 2 != 0:
        return False
    s = Stack()
    pairs = {'(': ')', '{': '}', '[': ']'}
    for i in line:
        if i in '({[':
            s.push(i)
        else:
            if len(s) == 0:
                return False
            top = s.pop()
            if pairs[top] != i:
                return False
    return True
def main():
    for line in sys.stdin:
        print(matcher(line.strip()))

if __name__ == '__main__':
    main()
