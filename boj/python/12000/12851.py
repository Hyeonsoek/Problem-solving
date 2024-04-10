from collections import deque
from collections import defaultdict

MAX = 987654321

start, end = map(int, input().split())

def bfs():

	q = deque()
	check = [ 0 for _ in range(100001) ]

	min_cost = MAX
	q.append((0, start))

	while q:
		cost, x = q.popleft()
		check[x] = 1

		if x == end:
			min_cost = cost
			break

		if 0 <= x - 1 and check[x-1] == 0:
			q.append((cost+1, x-1))

		if x + 1 <= 100000 and check[x+1] == 0:
			q.append((cost+1,x+1))

		if x * 2 <= 100000 and check[x*2] == 0:
			q.append((cost+1,x*2))

	count = 0
	q = deque()
	q.append((0, start))

	while q:
		cost, x = q.popleft()
		check[x] = 0

		if cost == min_cost and x == end:
			count += 1
		elif cost < min_cost:
			if 0 <= x - 1 and check[x-1] == 1:
				q.append((cost+1, x-1))
			if x + 1 <= 100000 and check[x+1] == 1:
				q.append((cost+1, x+1))
			if x * 2 <= 100000 and check[x*2] == 1:
				q.append((cost+1, x*2))

	return min_cost, count

result, count = bfs()
print(result)
print(count)