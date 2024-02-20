import sys
from math import atan2

# same problem boj 1310

input = sys.stdin.readline

def sub(a, b):
    return [a[0] - b[0], a[1] - b[1]]

def ccw(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    return (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)

def distance(a, b):
    ax, ay = a
    bx, by = b
    return (bx - ax) ** 2 + (by - ay) ** 2

def convex_hull(points, n):
    points.sort(key = lambda p: (p[1], p[0]))
    
    sx, sy = points[0]
    points[1:] = sorted(points[1:], key=lambda p: atan2(p[1] - sy, p[0] - sx))
    
    convex = [points[0], points[1]]
    for x in range(2, n):
        while len(convex) >= 2:
            first = convex[-1]
            second = convex[-2]
            if ccw(second, first, points[x]) > 0:
                break
            convex.pop()
        convex.append(points[x])
        
    return convex

def rotating_calipers(convex, n):
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
        
        if ccw([0, 0], pleft, pright) > 0:
            left = (left + 1) % n
        else:
            right = (right + 1) % n

        result = max(result, distance(convex[left], convex[right]))

    return result

n = int(input())
points = [ list(map(int, input().split())) for _ in range(n) ]
convex = convex_hull(points, n)
length = len(convex)
calipers = rotating_calipers(convex, length)
print(calipers)