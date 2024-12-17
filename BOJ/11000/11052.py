n = int(input())
cards = list(map(int, input().split()))

cache = [0] * 1001
cache[1] = cards[0]

for i in range(2, n+1):
	for j in range(1, i+1):
		cache[i] = max(cache[i], cache[i-j] + cards[j-1])

print(cache[n])