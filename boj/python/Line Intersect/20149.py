class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __le__(self, other):
        if self.x != other.x:
            return self.x <= other.x
        return self.y <= other.y
    
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y
    
    def __str__(self) -> str:
        return "{0} {1}".format(self.x, self.y)

def ccw(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

ax, ay, bx, by = map(int, input().split())
cx, cy, dx, dy = map(int, input().split())

a = Point(ax, ay)
b = Point(bx, by)
c = Point(cx, cy)
d = Point(dx, dy)

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
        
    if a <= d and c <= b:
        print(1)
        left = (b.x - a.x) * (d.y - c.y)
        right = (d.x - c.x) * (b.y - a.y)
        
        if left == right:
            if a == d and c < b:
                print(a)
            
            if a < d and b == c:
                print(b)
        else:
            if a == c or a == d:
                print(a)
            
            if b == c or b == d:
                print(b)
        
    else:
        print(0)
        
elif ab <= 0 and cd <= 0:
    print(1)
    
    dx_ab = a.x - b.x
    dy_ab = a.y - b.y
    dx_cd = c.x - d.x
    dy_cd = c.y - d.y
    t1 = a.x * b.y - a.y * b.x
    t2 = c.x * d.y - d.x * c.y
    
    upper_x = t1 * dx_cd - dx_ab * t2
    upper_y = t1 * dy_cd - dy_ab * t2
    under = dx_ab * dy_cd - dy_ab * dx_cd
    
    print(upper_x / under, upper_y / under)
else:
    print(0)