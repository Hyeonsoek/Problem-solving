def solve():
    n = int(input())
    cache = [0, 1, 0, 1, 0]
    for i in range(5, n + 1):
        cache.append(any(cache[i - j] for j in [1, 3, 4]) ^ 1)
    
    print('CY' if cache[n] else 'SK')

solve()