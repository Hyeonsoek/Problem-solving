class Vec:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def sub(self, other):
        return Vec(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def inner(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vec(x, y, z)
    
    def size(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** .5

def solve():
    ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())
    
    a = Vec(ax, ay, az)
    b = Vec(bx, by, bz)
    c = Vec(cx, cy, cz)

    u = b.sub(a)
    p = c.sub(a)
    q = c.sub(b)

    if p.inner(u) * q.inner(u) <= 0:
        result = u.cross(p).size() / u.size()
        print(result)
    else:
        print(min(p.size(), q.size()))
        
solve()