def solve():
    n = int(input())
    
    cache = [0, 1, 0, 1, 1]
    
    for i in range(5, n + 1):
        cache.append(not all(cache[i - x] for x in (1, 3, 4)))
    
    print('SK' if cache[n] else 'CY')

solve()