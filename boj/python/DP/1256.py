def solve():
    n, m, k = map(int, input().split())
    cache = [[1] + [0] * x + [1] for x in range(n + m + 1)]

    for nn in range(1, n + m + 1):
        for kk in range(1, nn + 1):
            cache[nn][kk] += min(1000000000, cache[nn - 1][kk] + cache[nn - 1][kk - 1])        
    
    def find(nn, mm, kk):
        if nn == 0:
            return mm * "z"
        if mm == 0:
            return nn * "a"
        
        choose_a = cache[nn + mm - 2][nn - 1]
        
        if choose_a >= kk:
            return 'a' + find(nn - 1, mm, kk)
        else:
            return 'z' + find(nn, mm - 1, kk - choose_a)
    
    if cache[n + m - 1][n] < k:
        return -1
        
    return find(n, m, k)
        
print(solve())