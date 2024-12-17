from sys import stdin

t = int(stdin.readline())

MOD = 1000000009
cache = [[0] * 4 for _ in range(100001)]

for i in range(1, 4):
	cache[i][i] = 1

for j in range(3, 100001):
	cache[j][1] += cache[j-1][2] + cache[j-1][3]
	cache[j][2] += cache[j-2][1] + cache[j-2][3]
	cache[j][3] += cache[j-3][1] + cache[j-3][2]

	for i in range(1, 4):
		cache[j][i] %= MOD

for _ in range(t):
	n = int(stdin.readline())
	print(sum(cache[n]) % MOD)