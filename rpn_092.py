from stack_092 import Stack
import sys

def calculator(line):
    s = Stack()
    two = '+-*/'
    one = 'nr'
    line = line.split()
    for i in line:
        if i not in two and i not in one:
            s.push(float(i))
        else:
            if i in two:
                int1 = s.pop()
                int2 = s.pop()
                if i == '+':
                    new = (int2) + (int1)
                elif i == '-':
                    new = (int2) - (int1)
                elif i == '*':
                    new = (int2) * (int1)
                else:
                    new = (int2) / (int1)
                s.push(new)
            else:
                int1 = s.pop()
                if i == 'r':
                    new = (int1) ** .5
                else:
                    new = -1 * (int1)
                s.push(new)
    new = s.pop()
    return new

def main():

    for line in sys.stdin:
        try:
            a = calculator(line.strip())
            print('{:.2f}'.format(a))
        except IndexError:
            print('Invalid RPN expression')

if __name__ == '__main__':
    main()
