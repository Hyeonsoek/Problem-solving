n = int(input())
cache = [0, 1]
for x in range(n-1):
    cache.append((cache[-2] + cache[-1]) % 1000000007)
print(cache[n])