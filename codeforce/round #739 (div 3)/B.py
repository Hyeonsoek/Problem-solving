t = int(input())

for _ in range(t):
	a, b, c = map(int, input().split())

	maxValue = max(a, b) - min(a, b)

	if ((maxValue >= a and maxValue < b) or (maxValue >= b and maxValue < a)) \
		 and c <= maxValue * 2:
		print(c - maxValue if c > maxValue else c + maxValue)
	else:
		print(-1)