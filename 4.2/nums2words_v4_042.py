import sys

def main():
    nums = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten'
    }
    tens = {
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }
    numsbig = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }
    s = sys.stdin.readlines()
    for lines in s:
        lines = lines.split()
        new = []
        for i in lines:
            if len(i) == 1 or int(i) == 10:
                new.append(nums[int(i)])
            elif len(i) == 2:
                if int(i) in tens:
                    new.append(tens[int(i)])
                elif int(i[0]) in numsbig:
                    if int(i[1]) == 0:
                        new.append(numsbig[int(i[0])])
                    else:
                        new.append(numsbig[int(i[0])] + "-" + nums[int(i[1])])
            else:
                new.append("one hundred")
        print(" ".join(new))
if __name__ == "__main__":
   main()
