import sys

sys.setrecursionlimit(10000000)

n = int(input())

MAX = 987654321
cache = [-1] * (n+1)

def dp(n):
	if n == 0:
		return 0
	elif n < 0:
		return MAX
	else:
		if cache[n] != -1:
			return cache[n]
		cache[n] = min(dp(n-5)+1,dp(n-3)+1)
		return cache[n]

result = dp(n)
print(result if result < MAX else -1)