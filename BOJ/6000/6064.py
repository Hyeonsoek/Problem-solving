import math

t = int(input())

for _ in range(t):
	M, N, x, y = map(int, input().split())

	check = False

	for xx in range(x-1, M*N, M):
		if xx % N == (y-1):
			print(xx+1)
			check = True
			break

	if not check:
		print(-1)