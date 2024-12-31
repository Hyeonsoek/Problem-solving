import math
MOD = 10 ** 9 + 7

def pow(a, n):
    res = 1
    while n > 0:
        if n & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        n >>= 1
    return res

def solve():
    n = int(input())
    
    t = 0
    for i in range(7):
        t += math.comb(n, i)
        t %= MOD
    
    if n <= 5:
        print(4 ** n)
    else:
        print((pow(2, 3 * n) * t) % MOD)

solve()