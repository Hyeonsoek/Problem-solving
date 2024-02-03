n = int(input())
cache = [ 0 for _ in range(n + 1) ]

def dp(x):
    if x <= 1:
        return 0
    
    for xx in range(1, x):
        cache[x] = max(cache[x], dp(xx) + dp(x - xx) + xx * (x - xx))
    
    return cache[x]

print(dp(n))