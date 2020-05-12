import sys

def main():
    top_mark = 0
    inp = sys.argv[1]
    top_student1 = ""
    l = []
    with open(inp) as f:
        lines = f.readlines()
    for line in lines:
        try:
            line = line.strip().split()
            if int(line[0]) > top_mark:
                top_mark = int(line[0])
                top_student = line[1:]
                top_student = " ".join(top_student)
                l = [top_student]
            elif int(line[0]) == top_mark:
                top_mark = int(line[0])
                top_student = line[1:]
                top_student = " ".join(top_student)
                l.append(top_student)
        except:
            print('Invalid mark {} encountered. Skipping.'.format(line[0]))
    l = ', '.join(l)
    print('Best student(s):' + " " + l)
    print("Best mark:", top_mark)
if __name__ == '__main__':
    main()
