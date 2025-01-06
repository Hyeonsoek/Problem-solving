import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = sorted([int(input()) for _ in range(n)])

    result = -1
    for x in range(2, n):
        if arr[x-2] + arr[x-1] > arr[x]:
            result = arr[x-2] + arr[x-1] + arr[x]

    print(result)
    
solve()