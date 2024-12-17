import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    
    cache = [[0] * n for _ in range(m)]
    for x in range(m):
        cache[x][0] = arr[x][0]
    
    for x in range(1, n):
        for y in range(m):
            maxvalue = 0
            for yy in range(m):
                if y == yy:
                    maxvalue = max(maxvalue, cache[yy][x-1] + (arr[y][x] >> 1))
                else:
                    maxvalue = max(maxvalue, cache[yy][x-1] + arr[y][x])
            cache[y][x] = maxvalue
    
    rr = 0
    for x in range(m):
        rr = max(rr, cache[x][n-1])
    
    print(rr)
            
solve()