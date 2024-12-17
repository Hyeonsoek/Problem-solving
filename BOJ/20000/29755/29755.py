import sys
from bisect import *
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    black = sorted([*map(int, input().split())])

    def getValue(a, w, b):
        return abs(a - b) * w

    result = 0
    for _ in range(m):
        a, w = map(int, input().split())
        left = bisect_left(black, a, 0, n - 1) - 1
        
        value = 2 * 10 ** 8
        if left < n - 1:
            value = min(value, getValue(a, w, black[left + 1]))
        
        if left >= 0:
            value = min(value, getValue(a, w, black[left]))
        
        result = max(value, result)
    
    print(result)

solve()