def solve():
    n, m = map(int, input().split())
    edgs = set()

    k = int(input())
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        edgs.add((b, a, d, c))

    cache = [[0] * (n + 1) for _ in range(m + 1)]
    cache[0][0] = 1
    for y in range(m + 1):
        for x in range(n + 1):
            if (y, x-1, y, x) not in edgs and (y, x, y, x-1) not in edgs:
                cache[y][x] += cache[y][x-1]
            if (y-1, x, y, x) not in edgs and (y, x, y-1, x) not in edgs:
                cache[y][x] += cache[y-1][x]

    print(cache[m][n])

solve()