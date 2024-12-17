import sys, math
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
            return left > right
        
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x
    
    def set_vector(self, other):
        self.vx = self.x - other.x
        self.vy = self.y - other.y
        
    def __str__(self) -> str:
        return str(self.x) + " " + str(self.y)

def ccw(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def distance(vx, vy):
    return (vx ** 2 + vy ** 2) ** .5

def triagle_area(a, b, c):
    dx_ab, dy_ab = b.x - a.x, b.y - a.y
    dx_ac, dy_ac = c.x - a.x, c.y - a.y
    
    ab = distance(dx_ab, dy_ab)
    ac = distance(dx_ac, dy_ac)
    
    algebra = dx_ab * dx_ac + dy_ab * dy_ac
    geometry = ab * ac
    
    cos = algebra / geometry if geometry else 0
    theta = math.acos(cos)
        
    return 0.5 * ab * ac * math.sin(theta)

n = int(input())
inputs = sorted([ Point(*map(int, input().split())) for _ in range(n) ])

for x in range(1, n):
    inputs[x].set_vector(inputs[0])

inputs[1:] = sorted(inputs[1:])

convex = [0, 1]
for x in range(2, n):
    while len(convex) >= 2:
        first = convex.pop()
        second = convex[-1]
        
        if ccw(inputs[second], inputs[first], inputs[x]) > 0:
            convex.append(first)
            break
    convex.append(x)

result = 0
count = len(convex)
for x in range(1, count - 1):
    first = inputs[convex[0]]
    second = inputs[convex[x]]
    third = inputs[convex[x+1]]
    result += triagle_area(first, second, third)
    
print(int(result // 50))