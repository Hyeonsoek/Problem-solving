N = int(input())

MAX = 987654321
cache = [MAX for _ in range(N+1)]

cache[1] = 0

for x in range(2, N+1):
	if x % 2 == 0:
		cache[x] = min(1 + cache[x-1], 1 + cache[x//2])
	if x % 3 == 0:
		cache[x] = min(1 + cache[x-1], 1 + cache[x//3], cache[x])
	cache[x] = min(cache[x], cache[x-1] + 1)

print(cache[N])
print(*cache)