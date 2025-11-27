def solve():
    n = int(input())
    cache = [0] * (n + 3)
    cache[1] = 0
    cache[2] = 0
    cache[3] = 1

    for i in range(4, n + 1):
        cache[i] = min(1^cache[i-1], 1^cache[i-2], 1^cache[i-3])

    return cache[n]

print(solve() + 1)