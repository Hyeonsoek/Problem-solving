from sys import stdin

t = int(stdin.readline())

MOD = 1000000009
cache = [0] * 1000001

cache[0] = 1
for j in range(1, 1000001):
	for i in range(1, 4):
		if j >= i:
			cache[j] += cache[j-i]
			cache[j] %= MOD

for _ in range(t):
	n = int(stdin.readline())
	print(cache[n])