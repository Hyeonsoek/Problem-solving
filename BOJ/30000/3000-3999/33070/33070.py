import sys
from bisect import *
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = sorted(map(int, input().split()))
    data = [*map(int, input().split())]
    
    high = 0
    low = 0
    for i in range(n):
        if data[i]:
            l = min(bisect_left(arr, low), k - 1)
            r = bisect_right(arr, high) - 1
            
            if r < 0:
                continue
            
            if arr[l] >= low and high >= arr[r] and l <= r:
                high += 1
            
        else:
            low += 1
            high += 1
    
    print(n - high)

solve()

# arr = [*range(0, 20, 2)]
# i = bisect_right(arr, 3) - 1
# print(arr[i])