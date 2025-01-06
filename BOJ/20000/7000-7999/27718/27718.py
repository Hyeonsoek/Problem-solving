import sys
from fractions import Fraction
MAX = sys.maxsize
input = sys.stdin.readline

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
    def __ne__(self, value):
        return not self.__eq__(value)
    
    def __lt__(self, value):
        if self.x != value.x:
            return self.x < value.x
        return self.y < value.y
    
    def __le__(self, value):
        return self.__eq__(value) or self.__lt__(value)

class Line:
    def __init__(self, sx, sy, ex, ey):
        self.s = Point(sx, sy)
        self.e = Point(ex, ey)
        self.slope = Fraction(MAX, 1) if ex == sx else Fraction(ey - sy, ex - sx)
        
        if ex < sx or (sx == ex and ey < sy):
            self.s, self.e = self.e, self.s
    
    def __eq__(self, value):
        return self.s == value.s and self.e == value.e

def ccw(a : Point, b : Point, c : Point):
    result = (a.x * b.y + b.x * c.y + c.x * a.y) - (b.x * a.y + c.x * b.y + a.x * c.y)
    return (1 if result > 0 else -1) if result else 0

def intersection(a : Line, b : Line):
    if a == b:
        return 3

    ccwASE = ccw(a.s, a.e, b.s) * ccw(a.s, a.e, b.e)
    ccwBSE = ccw(b.s, b.e, a.s) * ccw(b.s, b.e, a.e)
    
    if ccwASE == 0 and ccwBSE == 0:
        if a.slope == b.slope:
            if a.e == b.s or b.e == a.s:
                return 1
            if (a.s <= b.s < a.e) or\
                (b.s <= a.s < b.e):
                return 3
            return 0
        return 1
    
    if (ccwASE == 0 and ccwBSE < 0) or\
        (ccwASE < 0 and ccwBSE == 0):
        return 1
    
    if ccwASE < 0 and ccwBSE < 0:
        return 2

    return 0

def solve():
    n = int(input())
    line = [Line(*map(int, input().split())) for _ in range(n)]
    
    arr = [[4] * n for _ in range(n)]
    for x in range(n):
        for y in range(x, n):
            arr[x][y] = intersection(line[x], line[y])
            arr[y][x] = arr[x][y]
    
    for x in arr:
        print(''.join(map(str, x)))

solve()