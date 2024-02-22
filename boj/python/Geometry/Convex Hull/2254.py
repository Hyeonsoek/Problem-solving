import sys
input = sys.stdin.readline

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 1
        self.vy = 0
    
    def __lt__(self, other):
        left = self.vx * other.vy
        right = self.vy * other.vx
        if left != right:
            return right < left
        
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x

    def __str__(self) -> str:
        return "x : {0}, y : {1}".format(self.x, self.y)

def ccw(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def convex_hull():
    npoints = sorted([ [points[x], x] for x in range(n) if x not in already ])
    length = len(npoints)
    
    if length <= 2:
        return 0
    
    for i in range(1, length):
        npoints[i][0].vx = npoints[i][0].x - npoints[0][0].x
        npoints[i][0].vy = npoints[i][0].y - npoints[0][0].y
     
    npoints[1:] = sorted(npoints[1:])
    
    stack = [0, 1]
    next = 2
    
    while next < length:
        while len(stack) >= 2:
            first = stack.pop()
            second = stack[-1]
            
            if ccw(npoints[second][0], npoints[first][0], npoints[next][0]) > 0:
                stack.append(first)
                break
        
        stack.append(next)
        next += 1
    
    length = len(stack)
    count = 0
    for x in range(-1, length - 1):
        already.add(npoints[stack[x]][1])
        if ccw(target, npoints[stack[x]][0], npoints[stack[x + 1]][0]) > 0:
            count += 1
    
    if abs(count) == length:
        return 1
    else:
        return 0

n, px, py = map(int, input().split())
target = Point(px, py)
points = sorted([ Point(*map(int, input().split())) for _ in range(n) ])

result = 0
already = set()
while len(already) < n - 2:
    convex = convex_hull()
    if convex:
        result += 1
    else:
        break

print(result)

# 12 0 0
# 1 0
# -1 0
# 0 1
# 0 -1
# 2 0
# -2 0
# 0 2
# 0 -2
# 3 0
# -3 0
# 0 3
# 0 -3