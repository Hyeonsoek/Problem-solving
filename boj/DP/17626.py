n = int(input())
cache = [0, 1]

for x in range(2, n + 1):
    value = 1
    result = 100000
    while value * value <= x:
        result = min(result, cache[x - value * value])
        value += 1
    cache.append(result + 1)

print(cache[n])