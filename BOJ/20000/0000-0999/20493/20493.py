import sys
DRY = [0, -1, 0, 1]
DRX = [1, 0, -1, 0]
input = sys.stdin.readline

def solve():
    n, T = map(int, input().split())

    d = 0
    bt = 0
    sx, sy = 0, 0
    for x in range(n):
        t, s = input().split()
        t = int(t)
        sx += (t - bt) * DRX[d]
        sy += (t - bt) * DRY[d]
        bt = t
        if s == 'right':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

    sx += int(T - bt) * DRX[d]
    sy += int(T - bt) * DRY[d]
    
    print(sx, sy)

solve()