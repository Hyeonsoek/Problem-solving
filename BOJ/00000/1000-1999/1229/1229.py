MAX = 710

def solve():
    count = [x * (2 * x - 1) for x in range(1, MAX)]
    set_count = set(count)
    
    n = int(input())
    cache = [6] * (n + 1)
    cache[0] = 0
    
    for x in count:
        if x <= n:
            cache[x] = 1

    for x in range(1, n + 1):
        if x in set_count:
            continue
        
        for y in range(MAX):
            if count[y] <= x:
                cache[x] = min(cache[x], cache[x - count[y]] + 1)
            else:
                break

    print(cache[n])
    
solve()