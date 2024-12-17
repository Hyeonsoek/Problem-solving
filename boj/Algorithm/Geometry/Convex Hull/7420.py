import sys, math
input = sys.stdin.readline

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
    
    def __lt__(self, other):
        left = self.vx * other.vy
        right = self.vy * other.vx
        if left != right:
            return left > right
        
        if self.y != other.y:
            return self.y < other.y

        return self.x < other.x

    def __str__(self) -> str:
        return "x : {0}, y : {1}".format(self.x, self.y)

def ccw(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def inner_product(a, b, c):
    return (a.x - b.x) * (c.x - b.x) + (a.y - b.y) * (c.y - b.y)

def distance(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

def angle(a, b, c):
    size_ab = distance(b, a)
    size_bc = distance(b, c)
    inner = inner_product(a, b, c)
    
    return math.acos(inner / (size_ab * size_bc))

n, l = map(int, input().split())
points = sorted([ Point(*map(int, input().split())) for _ in range(n) ])

for i in range(1, n):
    points[i].vx = points[i].x - points[0].x
    points[i].vy = points[i].y - points[0].y

points[1:] = sorted(points[1:])

stack = [0, 1]
next = 2

while next < n:
    while len(stack) >= 2:
        first = stack.pop()
        second = stack[-1]
        
        if ccw(points[second], points[first], points[next]) > 0:
            stack.append(first)
            break
    
    stack.append(next)
    next += 1
    
result = 0
for x in range(-2, len(stack) - 2):
    a = points[stack[x]]
    b = points[stack[x+1]]
    c = points[stack[x+2]]
    
    # a-b, b-c angle * L
    result += (math.pi - angle(a, b, c)) * l
    # a-b distance
    result += distance(a, b)
    
def rround(x):
    return int(x) + (1 if x - int(x) >= 0.5 else 0)
    
print(rround(result))