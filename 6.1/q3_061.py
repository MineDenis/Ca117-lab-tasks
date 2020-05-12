import sys

def main():
   string = sys.argv[1]
   s = list(string)
   for i in range(1, len(string), 2):
      s[i - 1], s[i] = s[i], s[i - 1]
   print("".join(s))
if __name__ == '__main__':
   main()
