def solve():
    a, b = input(), input()
    cache = [[0] * (len(b)+1) for _ in range(len(a)+1)]

    result = 0
    for x in range(1, len(a)+1):
        for y in range(1, len(b)+1):
            if a[x-1] == b[y-1]:
                cache[x][y] = cache[x - 1][y - 1] + 1
                result = max(result, cache[x][y])

    print(result)

solve()