import sys
from math import atan2
input = sys.stdin.readline

def sub(a, b):
    return ( a[0] - b[0], a[1] - b[1] )

def ccw(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    return (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)

def distance(a, b):
    ax, ay = a
    bx, by = b
    return ((bx - ax) ** 2 + (by - ay) ** 2)

t = int(input())
for _ in range(t):
    n = int(input())
    points = []
    for _ in range(n):
        sx, sy, length = map(int, input().split())
        points.append((sx, sy))
        points.append((sx + length, sy))
        points.append((sx, sy + length))
        points.append((sx + length, sy + length))
    n *= 4
    
    points.sort(key=lambda p: (p[1], p[0]))
    sx, sy = points[0]
    points[1:] = sorted(points[1:], key=lambda p: atan2(p[1]-sy, p[0]-sx))
    
    convex = [points[0], points[1]]
    for x in range(2, n):
        while len(convex) >= 2 and ccw(convex[-2], convex[-1], points[x]) <= 0:
            convex.pop()
        convex.append(points[x])
    n = len(convex)
    
    left, right = 0, 0
    for x in range(1, n):
        if convex[left][0] > convex[x][0]:
            left = x
        if convex[right][0] < convex[x][0]:
            right = x
    
    result = distance(convex[left], convex[right])
    for x in range(n):
        pleft = sub(convex[(left + 1) % n], convex[left])
        pright = sub(convex[right], convex[(right + 1) % n])
        
        if ccw((0, 0), pleft, pright) > 0:
            left = (left + 1) % n
        else:
            right = (right + 1) % n
        
        result = max(result, distance(convex[left], convex[right]))
    
    print(result)