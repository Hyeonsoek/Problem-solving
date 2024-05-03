import sys
input = sys.stdin.readline

class Point:
    def __init__(self, x, y, vx = 1, vy = 0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def __lt__(self, other):
        left = self.vx * other.vy
        right = self.vy * other.vx
        if left != right:
            return left > right
        
        if self.y != other.y:
            return self.y < other.y

        return self.x < other.x
    
def ccw(p1, p2, p3):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
        
n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

points.sort()

for i in range(1, n):
    points[i].vx = points[i].x - points[0].x
    points[i].vy = points[i].y - points[0].y

points[1:] = sorted(points[1:])

stack = [0, 1]
next = 2

while next < n:
    while len(stack) >= 2:
        first, second = stack.pop(), stack[-1]
        
        if ccw(points[second], points[first], points[next]) > 0:
            stack.append(first)
            break
    
    stack.append(next)
    next += 1

print(len(stack))