import sys

def main():
   for lines in sys.stdin:
      line = lines.strip()
      l = [char for char in line.lower() if char in "nice"]
      if l == list("nice"):
         print(line)


if __name__ == '__main__':
   main()
