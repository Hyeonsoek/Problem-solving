n = int(input())

cache = [1, 2, 3, 4, 5]

for x in range(5, n):
    value = cache[x-1] + 1
    for xx in range(x - 1):
        value = max(value, cache[xx] * (x - xx - 1))
    cache.append(value)

print(cache[n-1])