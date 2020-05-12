import sys

if __name__ == '__main__':
    top_mark = 0
    inp = sys.argv[1]
    with open(inp) as f:
        lines = f.readlines()
    try:
        for line in lines:
            line = line.strip().split()
            if int(line[0]) > top_mark:
                top_mark = int(line[0])
                top_student = line[1:]
            else:
                pass
        top_student = " ".join(top_student)
    except:
        print(Invalid mark "line[0]" encountered. Exiting.)
    print('Best student:' + " " + top_student)
    print("Best mark:", top_mark)
