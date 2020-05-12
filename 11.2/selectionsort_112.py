import random

def selectionsort(n):
    i = 0
    while i < len(n):
        j = i + 1
        p = i
        while j < len(n):
            if n[j] < n[p]:
                p = j
            j += 1
        tmp = n[p]
        n[p] = n[i]
        n[i] = tmp
        i += 1

def main():
    A = random.sample(range(-99, 100), 10)

    print('Unsorted: {}'.format(A))
    selectionsort(A)
    print('Sorted: {}'.format(A))

if __name__ == '__main__':
    main()
