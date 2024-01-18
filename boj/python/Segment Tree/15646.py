import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
tree = [[0] * (n + 2) for _ in range(m + 2)]

def update(y, x, value):
    while y <= m:
        px = x
        while px <= n:
            tree[y][px] += value
            px += px & -px
        y += y & -y
        
def sum(y, x):
    result = 0
    while y:
        px = x
        while px:
            result += tree[y][px]
            px -= px & -px
        y -= y & -y
    return result

for _ in range(q):
    q = list(map(int, input().split()))
    
    if q[0] & 1:
        _, x1, y1, x2, y2, d = q
        update(y1, x1, d)
        update(y2 + 1, x1, -d)
        update(y1, x2 + 1, -d)
        update(y2 + 1, x2 + 1, d)
    else:
        _, x, y = q
        print(sum(y, x))