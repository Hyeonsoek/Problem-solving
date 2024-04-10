import sys

from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = [ list(sys.stdin.readline().strip()) for _ in range(N) ]

def bfs():

	q = deque()
	dirr = [[0, 1],[0, -1],[1, 0],[-1, 0]]
	check = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

	q.append((0, 0, 0, 1)) #y, x, is_destruct, cost
	check[0][0][0] = 1

	answer = 987654321

	while q:
		y, x, is_destruct, cost = q.popleft()

		if y == N-1 and x == M-1 and answer > cost:
			answer = cost
			continue

		for ydir, xdir in dirr:
			yy = y + ydir
			xx = x + xdir

			if 0 <= yy < N and 0 <= xx < M:
				if is_destruct == 0 and check[1][yy][xx] == 0 and board[yy][xx] == '1':
					check[1][yy][xx] = 1
					q.append((yy, xx, 1,cost+1))

				if check[is_destruct][yy][xx] == 0 and board[yy][xx] == '0':
					check[is_destruct][yy][xx] = 1
					q.append((yy, xx, is_destruct, cost+1))

	return -1 if answer == 987654321 else answer

print(bfs())