import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    sx = sy = sxx = sxy = 0
    for _ in range(n):
        x, y = map(int, input().split())
        sx += x
        sy += y
        sxx += x * x
        sxy += x * y
    
    if sx * sx != n * sxx:
        a2 = (n * sxy - sx * sy) / (n * sxx - sx * sx)
        b2 = (sy - a2 * sx) / n
        print(a2, b2)
    else:
        print('EZPZ')

solve()