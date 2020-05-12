import sys

def prime(N):
  for i in range(2, N):
    if N % i == 0:
      return False
  return True
def main():
    N = int(sys.argv[1]) + 1
    nums = list(range(1, N))
    num = list(range(2, N))
    print("Multiples of 3: {}".format([i for i in nums if not i % 3]))
    print("Multiples of 3 squared: {}".format([i ** 2 for i in nums if not i % 3]))
    print("Multiples of 4 doubled: {}".format([i * 2 for i in nums if not i % 4]))
    print("Multiples of 3 or 4: {}".format([i for i in nums if not i % 3 or not i % 4]))
    print("Multiples of 3 and 4: {}".format([i for i in nums if not i % 3 and not i % 4]))
    print("Multiples of 3 replaced: {}".format([i if i % 3 else "X" for i in nums]))
    print("Primes: {}".format([i for i in num if prime(i)]))
if __name__ == "__main__":
    main()
