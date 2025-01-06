n = int(input())
cache = [0] * n
cache[0] = cache[1] = 1
for x in range(2, n):
    cache[x] = cache[x-1] + cache[x-2]

print(cache[n - 1], n - 2)