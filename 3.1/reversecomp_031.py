import sys

def bsearch(a, q):
   low = 0
   high = len(a)
   while low < high:
      mid = int((low + high) / 2)
      if a[mid] < q:
         low = mid + 1
      else:
         high = mid
   if a[low].lower().strip() == q:
      return True
   else:
      return False
def main():
   s = [word.strip() for word in sys.stdin]
   sl = [word.lower() for word in s]

   line = []
   for i in range(0, len(s)):
      if len(sl[i]) > 4:
         if bsearch(sl, sl[i][::-1]):
            line.append(s[i])
   print(line)
if __name__ == "__main__":
    main()
