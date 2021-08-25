n = int(input())

MOD = 1000000000

cache = [[0] * 10 for _ in range(n+1)]
cache[1] = [0] + [1] * 9

for i in range(2, n+1):
	for j in range(10):
		if j - 1 >= 0:
			cache[i][j] += cache[i-1][j-1]
			cache[i][j] %= MOD
		if j + 1 <= 9:
			cache[i][j] += cache[i-1][j+1]
			cache[i][j] %= MOD

print(sum(cache[n]) % MOD)