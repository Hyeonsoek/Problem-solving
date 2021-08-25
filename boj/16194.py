n = int(input())
cards = list(map(int, input().split()))

cache = [987654321] * (n+1)
cache[0] = 0
cache[1] = cards[0]

for i in range(2, n+1):
	for j in range(1, i+1):
		cache[i] = min(cache[i], cache[i-j] + cards[j-1])

print(cache[n])