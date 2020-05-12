import sys

def main():
   for lines in sys.stdin:
      line = lines.strip().split()
      for char in line:
         if line.count(char) == 1:
            print(char)
            break

if __name__ == '__main__':
   main()
