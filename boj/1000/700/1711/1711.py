import sys, math
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]

    result = 0
    for a in range(n):
        x1, y1 = arr[a]
        line = defaultdict(int)
        for b in range(n):
            if a == b:
                continue
            
            x2, y2 = arr[b]
            dx, dy = x2 - x1, y2 - y1
            gcd = math.gcd(dx, dy)
            
            dx //= gcd
            dy //= gcd
            
            line[dx, dy] += 1
            
        for (dx, dy), value in line.items():
            if (-dy, dx) in line:
                result += value * line[-dy, dx]
                
    print(result)
    
solve()

# print(math.gcd(-2, 4))