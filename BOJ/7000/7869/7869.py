from math import pi, acos, sin

def solve():
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
    
    if dist >= r1 + r2:
        return '0.000'

    if dist <= abs(r2 - r1):
        return f'{(min(r1, r2) ** 2) * pi:.3f}'

    theta1 = 2 * acos((r1 ** 2 + dist ** 2 - r2 ** 2) / (2 * r1 * dist))
    theta2 = 2 * acos((r2 ** 2 + dist ** 2 - r1 ** 2) / (2 * r2 * dist))
    
    area1 = (r1 ** 2) * (theta1 - sin(theta1)) / 2
    area2 = (r2 ** 2) * (theta2 - sin(theta2)) / 2
    
    return f'{area1 + area2:.3f}'

print(solve())