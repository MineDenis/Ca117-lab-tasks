import sys

def sorter(t):
   return t[-1]

def main():
   dis = []
   dic = {}
   for lines in sys.stdin:
      line = lines.strip().split()
      name, points = line[:-5], line[-5:]
      name = " ".join(name)
      total = 0
      try:
         for i in points:
            total += int(i)
      except ValueError:
         dis.append(name)
         pass
      else:
         dic[name] = total
   key_w = len(max(dic.keys(), key=len))
   key_l = len(str(max(dic.values())))
   for k, v in sorted(dic.items(), key=sorter, reverse=True):
      print("{:>{}}: {:{}} points".format(k, key_w, v, key_l))
   print("Disqualified:")
   for i in dis:
      print(i)

if __name__ == '__main__':
   main()
