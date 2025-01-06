import sys
input = sys.stdin.readline

def ccw(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

def intersect(ax, ay, bx, by, cx, cy, dx, dy):
    ccwABC = ccw(ax, ay, bx, by, cx, cy)
    ccwABD = ccw(ax, ay, bx, by, dx, dy)
    ccwCDA = ccw(cx, cy, dx, dy, ax, ay)
    ccwCDB = ccw(cx, cy, dx, dy, bx, by)
    
    ab = ccwABC * ccwABD
    cd = ccwCDA * ccwCDB
    
    if ab == 0 and cd == 0:
        return min(ax, bx) <= max(cx, dx) and min(cx, dx) <= max(ax, bx) and\
            min(ay, by) <= max(cy, dy) and min(cy, dy) <= max(ay, by)
    
    return ab <= 0 and cd <= 0

def solve():
    n = int(input())
    line = [0]
    for i in range(n):
        line.append(tuple(map(int, input().split())))

    parent = [i for i in range(n + 1)]
    
    def find(u):
        if parent[u] == u:
            return u
        parent[u] = find(parent[u])
        return parent[u]

    def merge(u, v):
        u = find(u)
        v = find(v)
        
        if u == v:
            return False

        parent[u] = v
        return True

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            ax, ay, bx, by = line[i]
            cx, cy, dx, dy = line[j]
            if intersect(ax, ay, bx, by, cx, cy, dx, dy):
                merge(i, j)
    
    group = [0] * (n + 1)
    for i in range(1, n + 1):
        group[find(i)] += 1
    
    groupCount = 0
    maxCount = 0
    for i in range(1, n + 1):
        if group[i] > 0:
            groupCount += 1
        maxCount = max(maxCount, group[i])
    
    print(groupCount)
    print(maxCount)

solve()