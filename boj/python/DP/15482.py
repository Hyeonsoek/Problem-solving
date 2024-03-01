def solve():
    a, b = input(), input()
    n, m = len(a), len(b)

    cache = [[0] * (n + 1) for _ in range(m + 1)]

    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if a[y - 1] == b[x - 1]:
                cache[x][y] = cache[x-1][y-1] + 1
            else:
                cache[x][y] = max(cache[x-1][y], cache[x][y-1])

    print(cache[m][n])
    
solve()