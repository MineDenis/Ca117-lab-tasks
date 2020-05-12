import sys
import math

def dist(x1, x2, y1, y2):
   return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
def main():
   xl = []
   yl = []
   for line in sys.stdin:
      line = line.strip().split()
      xl.append(int(line[0]))
      yl.append(int(line[1]))
   d1 = dist(xl[0], xl[1], yl[0], yl[1])
   d2 = dist(xl[0], xl[2], yl[0], yl[2])
   d3 = dist(xl[1], xl[2], yl[1], yl[2])
   if d1 == d2:
      x, y = (xl[1] + xl[2] - xl[0])s, (yl[1] + yl[2] - yl[0])
   elif d1 == d3:
      x, y = (xl[0] + xl[2] - xl[1]), (yl[0] + yl[2] - yl[1])
   else:
      x, y = (xl[0] + xl[1] - xl[2]), (yl[0] + yl[1] - yl[2])
   print(x, y)
if __name__ == '__main__':
   main()
