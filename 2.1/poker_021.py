#!/usr/bin/env python3

import sys

def main():

    nothing = 0
    one_p = 0
    two_p = 0
    ToK = 0
    stra = 0
    flus = 0
    full_h = 0
    FoK = 0
    stra_f = 0
    royal = 0
    total = 0
    for lines in sys.stdin:
        numbers = lines.strip().split()
        for digit in numbers:
            last_num = digit[-1]

            if last_num == "0":
                nothing += 1

            if last_num == "1":
                one_p += 1

            if last_num == "2":
                two_p += 1

            if last_num == "3":
                ToK += 1

            if last_num == "4":
                stra += 1

            if last_num == "5":
                flus += 1

            if last_num == "6":
                full_h += 1

            if last_num == "7":
                FoK += 1

            if last_num == "8":
                stra_f += 1

            if last_num == "9":
                royal += 1

    total = nothing + one_p + two_p + ToK + stra + flus + full_h + FoK + royal
    print(total)

    print(("The probabilty of nothing is {:.4f}%").format((nothing / total) * 100))
    print(("The probabilty of one pair is {:.4f}%").format(one_p / total * 100))
    print(("The probabilty of two pairs is {:.4f}%").format(two_p / total * 100))
    print(("The probabilty of three of a kind is {:.4f}%").format(ToK / total * 100))
    print(("The probabilty of a straight is {:.4f}%").format(stra / total * 100))
    print(("The probabilty of a flush is {:.4f}%").format(flus / total * 100))
    print(("The probabilty of a full house is {:.4f}%").format(full_h / total * 100))
    print(("The probabilty of four of a kind is {:.4f}%").format(FoK / total * 100))
    print(("The probabilty of a straight flush is {:.4f}%").format(stra_f / total * 100))
    print(("The probabilty of a royal flush is {:.4f}%").format(royal / total * 100))

if __name__ == '__main__':
    main()
