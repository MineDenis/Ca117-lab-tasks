import sys
import datetime

def lol(a):
    return a[1]

def main():
    dic = {}
    for line in sys.stdin:
        try:
            tokens = line.strip().split()
            name, time = tokens[0], tokens[1:]
            l = []
            for i in range(len(time)):
                seconds = time[i].split(":")
                total = int(seconds[0]) * 60 + int(seconds[1])
                l.append(total)
        except ValueError:
            pass
        dic[name] = min(l)
    name, time = min(dic.items(), key=lol)
    new_time = str(datetime.timedelta(seconds=time))
    print("{} : {}".format(name, new_time[3:]))
if __name__ == "__main__":
    main()
