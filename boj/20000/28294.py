MOD = 10 ** 9 + 7

def fast(a, n):
    result = 1
    while n:
        if n & 1:
            result = (a * result) % MOD
        a = (a * a) % MOD
        n >>= 1
    return result

def solve():
    n, a = map(int, input().split())
    back = (fast(n, a) - fast(n - 1, a)) % MOD
    left = fast(n - 1, a)
    print(((((n - 1) * back) % MOD + left) % MOD) * n % MOD)
    
solve()