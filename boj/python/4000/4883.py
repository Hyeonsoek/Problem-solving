import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline
MAX = 1_000_000_000

dirr = [
    [(0, 1), (1, 1), (1, 0)],
    [(1, -1), (1, 0), (1, 1), (0, 1)],
    [(1, -1), (1, 0)]
]

def solve(n):
    arr = [list(map(int, input().split())) for _ in range(n)]
    cache = [[MAX+1] * 3 for _ in range(n)]
    
    cache[n-1][1] = arr[n-1][1]
    cache[n-1][2] = MAX

    def dp(sx, sy):
        if cache[sx][sy] != MAX+1:
            return cache[sx][sy]
        
        result = MAX
        for dx, dy in dirr[sy]:
            xx = sx + dx
            yy = sy + dy
            if 0 <= xx < n and 0 <= yy < 3:
                result = min(result, arr[sx][sy] + dp(xx, yy))
        
        cache[sx][sy] = result
        return result

    return dp(0, 1)

count = 1
while True:
    n = int(input())
    
    if n == 0:
        break
    else:
        print(f'{count}. {solve(n)}')
        count += 1