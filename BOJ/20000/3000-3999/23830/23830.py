import sys
from bisect import *
MAX = 20_000_000_000
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = sorted([*map(int, input().split())])
    p, q, r, S = map(int, input().split())
    sumvalue = sum(arr)
    
    L = 1
    R = MAX
    result = sys.maxsize
    while L <= R:
        M = (L + R) >> 1
        
        greatorMr = n - bisect_right(arr, M + r)
        lessM = bisect_left(arr, M)
        value = sumvalue - greatorMr * p + lessM * q
        
        if value >= S:
            R = M - 1
            result = min(result, M)
        else:
            L = M + 1
    
    if result == sys.maxsize:
        return -1
    return result

print(solve())