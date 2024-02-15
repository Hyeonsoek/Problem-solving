import sys
input = sys.stdin.readline

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.vx = 1
        self.vy = 0
    
    def __lt__(self, other):
        left = self.vx * other.vy
        right = self.vy * other.vx
        
        if left != right:
            return left > right
        
        if self.x != other.x:
            return self.x < other.x
        
        return self.y < other.y

    def __str__(self) -> str:
        return "{0} {1}".format(self.x, self.y)
    
def ccw(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

n = int(input())
points = []

for _ in range(n):
    x, y, yn = input().split()
    if yn == 'Y':
        points.append(Point(int(x), int(y)))
points.sort()

for i in range(1, len(points)):
    points[i].vx = points[i].x - points[0].x
    points[i].vy = points[i].y - points[0].y
    
points[1:] = sorted(points[1:])

reverse = len(points) - 1
while ccw(points[reverse], points[0], points[reverse-1]) == 0:
    reverse -= 1

points[reverse:] = points[reverse:][::-1]

print(len(points))
print(*points, sep='\n')