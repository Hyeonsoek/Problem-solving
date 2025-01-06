def solve():
    n = int(input())
    cache = [0] * (n + 1)
    for x in range(1, n + 1):
        for k in range(1, 7):
            cache[x] += ((cache[x - k] if x >= k else 0) + 1) / 6
    
    print(cache[n])

solve()