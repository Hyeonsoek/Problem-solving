import math

t = int(input())

for _ in range(t):
	x, y = map(int, input().split())

	n = 1

	while x < y:
		x += math.ceil(n/2)
		n += 1

	print(n-1)