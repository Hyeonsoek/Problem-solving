import sys
MAX = 10000
input = sys.stdin.readline

def solve():
    n = int(input())
    sx, sy = MAX, MAX
    ex, ey = -MAX, -MAX
    
    for i in range(n):
        xx, yy = map(int, input().split())
        sx = min(sx, xx)
        sy = min(sy, yy)
        ex = max(ex, xx)
        ey = max(ey, yy)
    
    print((ey - sy) * (ex - sx))

solve()