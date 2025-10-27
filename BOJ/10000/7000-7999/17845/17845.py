import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(k)]
    
    cache = [[0] * (n + 1) for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        value, weight = arr[i - 1]
        for j in range(1, n + 1):
            if j >= weight:
                cache[i][j] = max(cache[i - 1][j], 
                                  cache[i - 1][j - weight] + value)
            else:
                cache[i][j] = cache[i - 1][j]
    
    print(cache[k][n])
    
solve()