import sys

def sumfac(a):
   total = 0
   for i in range(1, a // 2 + 1):
      if a % i == 0:
         total += i
   return total
def isperfect(a):
   total = sumfac(a)
   if total == a:
      return True
   else:
      return False

def main():
   for lines in sys.stdin:
      line = lines.strip()
      line = int(line)
      print(isperfect(line))

if __name__ == '__main__':
   main()
