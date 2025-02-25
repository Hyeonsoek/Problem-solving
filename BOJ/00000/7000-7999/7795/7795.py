import sys
from bisect import *
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    
    result = 0
    for x in A:
        result += bisect_left(B, x)
    
    return result

t = int(input())
for _ in range(t):
    print(solve())