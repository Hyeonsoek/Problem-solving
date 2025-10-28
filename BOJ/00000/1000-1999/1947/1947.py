MOD = 1_000_000_000

def solve():
    n = int(input())
    
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    cache = [0] * (n + 1)
    cache[2] = 1
    cache[3] = 2
    for i in range(4, n + 1):
        cache[i] = (cache[i - 1] + cache[i - 2]) * (i - 1) % MOD
    
    return cache[n]

print(solve())