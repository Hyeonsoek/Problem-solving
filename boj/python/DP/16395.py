n, k = map(int, input().split())
cache = [[-1] * (n + 1) for _ in range(n + 1)]

def dp(nn, kk):
    if kk == 0 or kk == nn:
        return 1
    
    if cache[nn][kk] != -1:
        return cache[nn][kk]
    
    cache[nn][kk] = dp(nn - 1, kk) + dp(nn - 1, kk - 1)
    return cache[nn][kk]

print(dp(n-1, k-1))