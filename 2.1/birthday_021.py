import sys
import calendar

def main():
    h1 = int(sys.argv[3])
    h2 = int(sys.argv[2])
    h3 = int(sys.argv[1])
    p = calendar.weekday(h1, h2, h3)
    if p == 0:
        print("You were born on a Monday and Monday's child is fair of face.")
    elif p == 1:
        print("You were born on a Tuesday and Tuesday's child is full of grace.")
    elif p == 2:
        print("You were born on a Wednesday and Wednesday's child is full of woe.")
    elif p == 3:
        print("You were born on a Thursday and Thursday's child has far to go.")
    elif p == 4:
        print("You were born on a Friday and Friday's child is loving and giving.")
    elif p == 5:
        print("You were born on a Saturday and Saturday's child works hard for a living.")
    else:
        print("You were born on a Sunday and Sunday's child is fair and wise and good in every way.")
if __name__ == "__main__":
    main()
