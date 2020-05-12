import sys

def sorter(t):
   return t[-1]
def main():
   dic = {}
   s = sys.argv[1]
   with open(s) as fd:
      for lines in fd:
         line = lines.strip().split()
         letter, cost = line[0], int(line[1])
         dic[letter] = cost
   string = sys.argv[2]
   biggest = {}
   for lines in sys.stdin:
      list_string = list(string)
      points = []
      line = lines.strip()
      for c in line:
         if c in list_string:
            points.append(c)
            list_string.remove(c)
      biggest[line] = points
   score = []
   top = ""
   for k, v in biggest.items():
      if len(v) == len(score):
         if len(k) < len(top):
            top, score = k, v
            pass
      if len(v) > len(score):
         top, score = k, v
   total = 0
   for i in score:
      total += dic[i]
   print("{}: {}".format(top, total))
if __name__ == '__main__':
   main()
