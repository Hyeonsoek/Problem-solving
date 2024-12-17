n = int(input())
cache = [1, 1]
for x in range(2, n+1):
    value = 0
    for xx in range(x):
        value += cache[xx] * cache[x - xx - 1]
    cache.append(value)

print(cache[-1])