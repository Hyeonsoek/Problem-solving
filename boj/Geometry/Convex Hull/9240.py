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
            return left > right
        
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x
    
    def set_vector(self, other):
        self.vx = self.x - other.x
        self.vy = self.y - other.y
    
    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** .5

def ccw(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def convex_hull():
    convex = [0, 1]
    
    for x in range(2, n):
        while len(convex) >= 2:
            first = convex.pop()
            second = convex[-1]
            
            if ccw(points[second], points[first], points[x]) > 0:
                convex.append(first)
                break
            
        convex.append(x)
        
    return [ points[x] for x in convex ]

n = int(input())
points = sorted([ Point(*map(int, input().split())) for _ in range(n) ])

for i in range(1, n):
    points[i].set_vector(points[0])
points[1:] = sorted(points[1:])

result = 0
convex = convex_hull()
length = len(convex)
for x in range(length - 1):
    for y in range(x, length):
        distance = convex[x].distance_to(convex[y])
        if result < distance:
            result = distance

print(result)