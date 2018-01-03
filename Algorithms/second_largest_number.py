#!/bin/python3.5

if __name__ == '__main__':
    n = int(5)
    arr = list(map(int, "2 12 3 6 6 5 9".split()))
    arr = list(set(arr))
    arr.sort()
    print(arr[len(arr)-2])
