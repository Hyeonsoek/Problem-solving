## same to boj 17387

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __le__(self, other):
        if self.x != other.x:
            return self.x <= other.x
        return self.y <= other.y
    
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

def ccw(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def is_intersect(a : Point, b : Point, c : Point, d : Point):
    abc_ccw = ccw(a, b, c)
    abd_ccw = ccw(a, b, d)
    cda_ccw = ccw(c, d, a)
    cdb_ccw = ccw(c, d, b)
    
    ab = abc_ccw * abd_ccw
    cd = cda_ccw * cdb_ccw
    
    if ab == 0 and cd == 0:
        if a > b:
            a, b = b, a
            
        if c > d:
            c, d = d, c
            
        return a <= d and c <= b

    return ab <= 0 and cd <= 0

ax, ay, bx, by = map(int, input().split())
cx, cy, dx, dy = map(int, input().split())

a = Point(ax, ay)
b = Point(bx, by)
c = Point(cx, cy)
d = Point(dx, dy)

print(1 if is_intersect(a, b, c, d) else 0)