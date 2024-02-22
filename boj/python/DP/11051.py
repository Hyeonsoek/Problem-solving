import sys
sys.setrecursionlimit(10000)

n, k = map(int, input().split())

cache = [[-1] * (n+1) for _ in range(n+1)]

def dp(nn, rr):
    if rr == nn or rr == 0:
        return 1
    
    if cache[nn][rr] != -1:
        return cache[nn][rr]
    
    cache[nn][rr] = (dp(nn - 1, rr) + dp(nn - 1, rr - 1)) % 10007
    return cache[nn][rr]

print(dp(n, k))