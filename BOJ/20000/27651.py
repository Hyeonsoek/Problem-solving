import sys
from bisect import *
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    prefix = [arr[0]]
    for x in range(1, n):
        prefix.append(prefix[-1] + arr[x])
    length = prefix[-1]
    
    result = 0
    for x in range(n - 2):
        head = prefix[x]
        
        ll = (head + length) >> 1
        rr = length - head
        
        left = bisect_right(prefix, ll , x + 1, n - 1)
        right = bisect_left(prefix, rr, x + 1, n - 1)
        
        if left <= right:
            result += right - left
        
    print(result)

solve()