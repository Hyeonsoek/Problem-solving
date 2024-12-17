MOD = 1000000007

def fastexp(a, n):
    result = 1
    while n > 0:
        if n & 1:
            result *= a
            result %= MOD
        a *= a
        a %= MOD
        n //= 2
    
    return result

def factorial(n):
    result = 1
    for x in range(2, n + 1):
        result *= x
        result %= MOD
    return result

def solve():
    n, r = map(int, input().split())
    
    upper = factorial(n)
    lower_left = fastexp(factorial(n - r), MOD - 2)
    lower_right = fastexp(factorial(r), MOD - 2)
    
    lower = lower_left * lower_right % MOD
    result = upper * lower % MOD
    
    return result

print(solve())