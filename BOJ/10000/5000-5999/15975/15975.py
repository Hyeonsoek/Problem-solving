import sys
from collections import defaultdict
input = sys.stdin.readline
MAX = 10 ** 9 + 1

def solve():
    n = int(input())
    color = defaultdict(list)

    for _ in range(n):
        x, c = map(int, input().split())
        color[c].append(x)

    for key in color:
        color[key].sort()
        
    result = 0
    for pos in color.values():
        for x in range(len(pos)):
            value = MAX
            if x > 0:
                value = min(value, pos[x] - pos[x - 1])
                
            if x < len(pos) - 1:
                value = min(value, pos[x + 1] - pos[x])
            
            result += value if MAX != value else 0
            
    print(result)

solve()