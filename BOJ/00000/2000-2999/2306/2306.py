def solve():
    sqeunce = input()
    
    n = len(sqeunce)
    cache = [[0] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(n - i):
            s, e = j, j + i
            for k in range(s, e):
                cache[s][e] = max(cache[s][e], cache[s][k] + cache[k + 1][e])
            
            if (sqeunce[s] + sqeunce[e]) in ['at', 'gc']:
                cache[s][e] = max(cache[s][e], cache[s + 1][e - 1] + 2)
    
    print(cache[0][n - 1])

solve()