import sys

if __name__ == '__main__':
    top_mark = 0
    inp = sys.argv[1]
    with open(inp) as f:
        lines = f.readlines()
    for line in lines:
        try:
            line = line.strip().split()
            if int(line[0]) > top_mark:
                top_mark = int(line[0])
                top_student = line[1:]
        except:
            print('Invalid mark {} encountered. Skipping.'.format(line[0]))
    top_student = " ".join(top_student)
    print('Best student:' + " " + top_student)
    print("Best mark:", top_mark)
