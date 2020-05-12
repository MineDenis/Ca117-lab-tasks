import sys

def main():
    d = {}
    p = sys.argv[1]
    with open(p) as fd:
        fd = fd.readlines()
    for i in range(len(fd)):
        f = fd[i].split()
        d[i] = f[0], f[1]
    s = sys.stdin.readlines()
    for lines in s:
        lines = lines.split()
        new = []
        for i in lines:
            if int(i) in d:
                new.append(d[int(i)][1])
        print(" ".join(new))
if __name__ == "__main__":
   main()
