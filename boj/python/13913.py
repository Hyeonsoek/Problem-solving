from collections import deque

start, target = map(int, input().split())

def bfs():

	q = deque()
	check = [-1 for _ in range(100001)]

	result = 0
	check[start] = 0
	q.append(start)

	while q:
		route = q.popleft()

		if route == target:
			result = check[route]
			break

		if 0 <= route + 1 <= 100000 and check[route+1] == -1:
			check[route + 1] = check[route] + 1
			q.append(route + 1)

		if 0 <= route - 1 <= 100000 and check[route-1] == -1:
			check[route - 1] = check[route] + 1
			q.append(route - 1)

		if 0 <= route * 2 <= 100000 and check[route*2] == -1:
			check[route * 2] = check[route] + 1
			q.append(route * 2)

	q = deque()
	q.append(str(target))

	while q:
		route = q.popleft()
		point = int(route.split('/')[-1])

		if point == start:
			return result, route

		if 0 <= point + 1 <= 100000 and check[point+1] == check[point] - 1:
			q.append(route + '/' + str(point+1))

		if 0 <= point - 1 <= 100000 and check[point-1] == check[point] - 1:
			q.append(route + '/' + str(point-1))

		if point % 2 == 0 and 0 <= point // 2 <= 100000 \
			and check[point//2] == check[point] - 1:
			q.append(route + '/' + str(point//2))

	return -1, -1

if start <= target:
	result, route = bfs()

	print(result)
	print(*route.split('/')[::-1])
else:
	print(start - target)
	print(*range(start, target-1, -1))