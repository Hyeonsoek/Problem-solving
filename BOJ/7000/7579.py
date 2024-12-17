import sys
MAX = 10000
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    app = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    # maximum app memory in x cost
    cache = [[0] * (MAX + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(MAX + 1):
            if cost[i] <= j:
                cache[i+1][j] = max(app[i] + cache[i][j - cost[i]], cache[i][j])
            else:
                cache[i+1][j] = cache[i][j]

    for x in range(MAX + 1):
        if cache[n][x] >= m:
            return x
        
print(solve())