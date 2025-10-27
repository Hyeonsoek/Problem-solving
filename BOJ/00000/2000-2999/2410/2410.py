MOD = 1000000000

def solve():
    n = int(input()) // 2
    cache = [0] * (n + 1)
    cache[0] = 1
    for j in range(1, n + 1):
        cache[j] = (cache[j - 1] + cache[j // 2]) % MOD
    print(cache[n])

solve()