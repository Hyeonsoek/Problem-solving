import sys
from bisect import *
input = sys.stdin.readline

def solve():
    n = int(input())
    xindex, xvalue = [], []
    for _ in range(n):
        i, v = map(int, input().split())
        xindex.append(i)
        xvalue.append(v)
        
    m = int(input())
    yindex, yvalue = [], [0]
    for _ in range(m):
        i, v = map(int, input().split())
        yindex.append(i)
        yvalue.append(v)
    
    for x in range(1, m + 1):
        yvalue[x] += yvalue[x-1]
    
    a, b = int(input()), int(input())
    
    result = 0
    for x in range(n):
        s = bisect_left(yindex, xindex[x] + a)
        e = bisect_right(yindex, xindex[x] + b)
        result += xvalue[x] * (yvalue[e] - yvalue[s])
        
    print(result)

solve()