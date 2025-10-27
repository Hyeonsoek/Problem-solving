def solve():
    n = input()
    k = len(n)
    cache = [0] * (k + 1)
    cache[0] = cache[1] = 1
    for i in range(2, k + 1):
        if n[i - 1] != '0':
            cache[i] = cache[i - 1]
        if n[i - 2] != '0' and n[i - 2] + n[i - 1] <= '34':
            cache[i] += cache[i - 2]
    
    print(cache[k])

solve()