import sys
input = sys.stdin.readline

def get_x(x, s, e):
    if s <= x <= e:
        return e + 1
    return x

def solve():
    n, m = map(int, input().split())
    startX = 1
    for _ in range(n - 1):
        count, *remain = input().split()
        count = int(count)
    
        if count == 0:
            continue
        
        if count == 1:
            a, b = remain
            if b == 'L':
                startX = get_x(startX, 1, int(a))
            else:
                startX = get_x(startX, int(a), m)
        
        if count == 2:
            a, b, c, d = remain
            if b == 'L':
                startX = get_x(startX, 1, int(a))
            else:
                startX = get_x(startX, int(a), int(c))

            if d == 'L':
                startX = get_x(startX, int(a), int(c))
            else:
                startX = get_x(startX, int(c), m)
    
    return "YES" if startX <= m else "NO"

print(solve())