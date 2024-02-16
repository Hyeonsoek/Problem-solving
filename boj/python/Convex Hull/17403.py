import sys
input = sys.stdin.readline

class Point:
    def __init__(self, index, x, y):
        self.index = index
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
        
    def set_vector_1(self):
        self.vx = 1
        self.vy = 0
        
    def __str__(self) -> str:
        return str(self.x) + " " + str(self.y)

def ccw(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def convex_hull(points : list[Point], length):
    for i in range(length):
        points[i].set_vector_1()
    
    points.sort()
    
    for i in range(1, length):
        points[i].set_vector(points[0])
    
    points[1:] = sorted(points[1:])
    
    convex = [0, 1]
    for x in range(2, length):
        while len(convex) >= 2:
            first = convex.pop()
            second = convex[-1]
            
            if ccw(points[second], points[first], points[x]) > 0:
                convex.append(first)
                break
        convex.append(x)
    
    return convex

n = int(input())
inputs = [ Point(x, *map(int, input().split())) for x in range(n) ]

floor = 1
answer = [0] * n
while n >= 3:
    convex = convex_hull(inputs, n)
    
    if len(convex) <= 2:
        break
    
    for x in convex:
        answer[inputs[x].index] = floor
    
    inputs = [ inputs[x] for x in range(n) if x not in convex ]
    n -= len(convex)
    floor += 1

print(*answer)