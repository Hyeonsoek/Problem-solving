import sys
sys.setrecursionlimit(200000)

MAX = 999999

n = int(input())
cache = [ MAX ]*(n+1)

def dp(x):
    if x < 0:
        return MAX
    
    if x == 0:
        return 0
    
    if x == 2 or x == 5:
        return 1
    
    if cache[x] != MAX:
        return cache[x]
    
    cache[x] = min(cache[x], dp(x - 2) + 1, dp(x - 5) + 1)
    return cache[x]

result = dp(n)
print(-1 if result == MAX else result )