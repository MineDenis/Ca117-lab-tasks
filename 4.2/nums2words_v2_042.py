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
            try:
                if int(i) <= 10:
                    new.append(nums[int(i)])
                else:
                    new.append("unknown")
            except:
                new.append("unknown")
        print(" ".join(new))
if __name__ == "__main__":
   main()
