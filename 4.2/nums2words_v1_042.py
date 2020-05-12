import sys

def main():
    nums = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten'
    ]
    s = sys.stdin.readlines()
    for lines in s:
        lines = lines.split()
        new = []
        for i in lines:
            new.append(nums[int(i)])
        print(" ".join(new))
if __name__ == "__main__":
   main()
