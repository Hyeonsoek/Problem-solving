from itertools import permutations
from math import *

def get_angle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    vx1, vy1 = x1 - x2, y1 - y2
    vx2, vy2 = x3 - x2, y3 - y2
    o1 = atan2(vy1, vx1)
    o2 = atan2(vy2, vx2)
    result = (o1 - o2) * 180 / pi
    return result + (360 if result < 0 else 0)

def is_convex_polygon(distances):
    points = []
    for i in range(8):
        x = distances[i] * sin(i * pi / 4)
        y = distances[i] * cos(i * pi / 4)
        points.append((x, y))
    
    for i in range(8):
        angle = get_angle(points[i], points[(i + 1) % 8], points[(i + 2) % 8])
        if angle < 180:
            return 0
    
    return 1

def solve():
    distances = list(map(int, input().split()))
    count = 0
    for perm in permutations(distances):
        if is_convex_polygon(perm):
            count += 1
    
    print(count)

solve()