from collections import deque

def bfs():

	check = [[0]*N for _ in range(2)]
	q = deque()

	q.append((0, 0, 0))
	check[0][0] = 1

	while q:
		floor, line, second = q.popleft()

		# print(floor, line, second)

		if floor + k >= N:
			return 1
		elif second+1 <= floor + k < N and board[line^1][floor+k] == '1' \
				and check[line^1][floor+k] == 0:
			check[line^1][floor+k] = 1
			q.append((floor + k, line^1, second+1))

		for x in [-1, 1]:
			next_floor = floor + x
			if next_floor >= N:
				return 1
			if second+1 <= next_floor < N and board[line][next_floor] == '1' \
					and check[line][next_floor] == 0:
				check[line][next_floor] = 1
				q.append((next_floor, line, second+1))

	return 0
 
N, k = map(int, input().split())
board = [ input() for _ in range(2) ]

print(bfs())