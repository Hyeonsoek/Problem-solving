from sys import stdin

t = int(stdin.readline())

cache = [0] * 10001

cache[0] = 1
for i in range(1, 4):
	for j in range(i, 10001):
		cache[j] += cache[j-i]

for _ in range(t):
	n = int(stdin.readline())
	print(cache[n])