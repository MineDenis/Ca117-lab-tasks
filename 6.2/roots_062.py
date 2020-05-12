import sys
import math

def _b(a, b, c):
   return (- b + (math.sqrt(b ** 2 - 4 * a * c))) / (2 * a)
def __b(a, b, c):
   return (- b - (math.sqrt(b ** 2 - 4 * a * c))) / (2 * a)
def main():
   for lines in sys.stdin:
      try:
         line = lines.strip().split()
         r1 = _b(int(line[0]), int(line[1]), int(line[2]))
         r2 = __b(int(line[0]), int(line[1]), int(line[2]))
         print("r1 = {}, r2 = {}".format(r1, r2))
      except ValueError:
         print("None")
         pass
if __name__ == '__main__':
   main()
