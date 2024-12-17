import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n = int(input())
    coords = defaultdict(int)
    for _ in range(n):
        s, e = map(int, input().split())
        coords[s] += 1
        coords[e] -= 1

    coords = sorted(coords.items())
    
    prefix = 0
    result = 0
    for key, value in coords:
        prefix += value
        result = max(result, prefix)
    
    print(result)

solve()