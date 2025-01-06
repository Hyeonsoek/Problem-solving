from collections import deque

N, K = map(int, input().split())

def bfs():

	q = deque()
	check = [0 for _ in range(100001)]

	q.append((N,0))

	while q:
		x, time = q.popleft()
		check[x] = 1

		if x == K:
			print(time)
			break

		if 0 <= x - 1 <= 100000 and check[x-1] == 0:
			q.append((x-1, time+1))
			check[x-1] = 1

		if 0 <= x + 1 <= 100000 and check[x+1] == 0:
			q.append((x+1, time+1))

		if 0 < x * 2 <= 100000 and check[x*2] == 0:
			q.appendleft((x*2, time))
			check[x*2] = 1

bfs()