def dynamic(n, m):
    cache = [[0] * m for _ in range(n)]
        
    for i in range(n):
        cache[i][0] = 1

    for j in range(m):
        cache[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]

    return cache[n - 1][m - 1]

def solve():
    n, m, k = map(int, input().split())
    
    if k == 0:
        print(dynamic(n, m))
    else:
        r, c = divmod(k - 1, m)
        print(dynamic(r + 1, c + 1) * dynamic(n - r, m - c))

solve()