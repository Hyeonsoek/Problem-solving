cache = [1, 1, 1]
for x in range(3, int(input())):
    cache.append(cache[x-3] + cache[x-1])
print(cache[-1])