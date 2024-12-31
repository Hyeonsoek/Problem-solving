def getdistance(sx, sy, ex, ey):
    return (ex - sx) ** 2 + (ey - sy) ** 2

def solve():
    n, m = map(int, input().split())
    pos = []
    for _ in range(n):
        xx, yy = map(int, input().split())
        pos.append((xx, yy))
    
    result = 0
    sx = sy = 0
    for _ in range(m):
        dist = sorted([(getdistance(sx, sy, ex, ey), ex, ey) for ex, ey in pos])
        maxdist, xx, yy = dist.pop()
        sx = xx; sy = yy
        result += maxdist
        pos.remove((xx, yy))
        xx, yy = map(int, input().split())
        pos.append((xx, yy))
    
    print(result)

solve()