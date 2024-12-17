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

def convex_hull(points, nn):
    if nn == 1:
        return [ points[0], points[0] ]
    
    for i in range(1, nn):
        points[i].vx = points[i].x - points[0].x
        points[i].vy = points[i].y - points[0].y
    
    points[1:] = sorted(points[1:])
    
    convex = [0, 1]
    next = 2
    
    while next < nn:
        while len(convex) >= 2:
            first = convex.pop()
            second = convex[-1]
            
            if ccw(points[second], points[first], points[next]) > 0:
                convex.append(first)
                break
        
        convex.append(next)
        next += 1
    
    return [ points[x] for x in convex ]

def is_intersect(a : Point, b : Point, c : Point, d : Point):
    abc_ccw = ccw(a, b, c)
    abd_ccw = ccw(a, b, d)
    cda_ccw = ccw(c, d, a)
    cdb_ccw = ccw(c, d, b)
    
    ab = abc_ccw * abd_ccw
    cd = cda_ccw * cdb_ccw
    
    if ab == 0 and cd == 0:
        # compare a to d and b to c
        x_1 = min(a.x, b.x) <= max(c.x, d.x)
        x_2 = min(c.x, d.x) <= max(a.x, b.x)
        y_1 = min(a.y, b.y) <= max(c.y, d.y)
        y_2 = min(c.y, d.y) <= max(a.y, b.y)
        
        return x_1 and x_2 and y_1 and y_2

    return ab <= 0 and cd <= 0

def is_inner_convex(convex, others):
    length = len(convex)
    for point in others:
        count = 0
        for x in range(-1, length - 1):
            if ccw(convex[x], convex[x + 1], point) > 0:
                count += 1
        
        if count == length:
            return False
    
    return True

test = int(input())
answer = []
for _ in range(test):
    n, m = map(int, input().split())
    
    blacks = sorted([ Point(*map(int, input().split())) for _ in range(n) ])
    whites = sorted([ Point(*map(int, input().split())) for _ in range(m) ])
    
    result = True

    if n == 1 and m == 1:
        answer.append("YES")
        continue
    
    # 1. convex hull 선분 교차판정 (서로)
    # 2. convex hull 점 내부 판정 (서로)
    black_convex = convex_hull(blacks, n)
    white_convex = convex_hull(whites, m)
    
    black_len = len(black_convex)
    white_len = len(white_convex)
    
    for i in range(-1, black_len-1):
        for j in range(-1, white_len-1):
            a, b = black_convex[i], black_convex[i+1]
            c, d = white_convex[j], white_convex[j+1]
            result &= not is_intersect(a, b, c, d)
    
    result &= is_inner_convex(black_convex, white_convex)
    result &= is_inner_convex(white_convex, black_convex)
        
    answer.append("YES" if result else "NO")

print(*answer, sep='\n')
        
# 1
# 3 3
# 100 700
# 200 200
# 600 600
# 500 100
# 500 300
# 800 500

# 1
# 2 2
# 0 0
# 500 700
# 1000 1400
# 1500 2100