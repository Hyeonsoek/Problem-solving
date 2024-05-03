import sys
from math import atan2
input = sys.stdin.readline

def sub(a, b):
    return ( a[0] - b[0], a[1] - b[1] )

def ccw(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

def distance(a, b):
    ax, ay = a
    bx, by = b
    return ((bx - ax) ** 2 + (by - ay) ** 2) ** .5

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
        
    return convex, len(convex)

def rotating_calipers(convex, n):
    length = [ distance(convex[x], convex[(x + 1) % n]) for x in range(n) ]

    left, right = 0, 0
    for x in range(n):
        rx, ry = convex[right]
        xx, xy = convex[x]
        if ry < xy or (ry == xy and rx < xx):
            right = x
            
    current = 0
    index = left
    while index != right:
        current += length[index]
        index = (index + 1) % n
    result = current
    
    for x in range(2 * n):
        pleft = sub(convex[(left + 1) % n], convex[left])
        pright = sub(convex[right], convex[(right + 1) % n])
        product = ccw((0, 0), pleft, pright)
        
        if product >= 0:
            current -= length[left]
            left = (left + 1) % n
        
        if product <= 0:
            current += length[right]
            right = (right + 1) % n
        
        result = min(result, current)
        
    return result

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
convex, size = convex_hull(points, n)
print(rotating_calipers(convex, size))