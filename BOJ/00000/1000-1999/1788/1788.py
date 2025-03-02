MOD = 10 ** 9

def solve():
    n = int(input())
    
    cache = {0 : 0, 1 : 1}
    
    if n < 0:
        for i in range(1, abs(n) + 1):
            X = cache[-i+2] - cache[-i+1]
            X %= MOD if X > 0 else -MOD            
            cache[-i] = X
    else:
        for i in range(2, n + 1):
            cache[i] = (cache[i-1] + cache[i-2]) % MOD
    
    print(1 if cache[n] > 0 else (-1 if cache[n] < 0 else 0))
    print(abs(cache[n]) % MOD)
    
solve()