import sys
from collections import deque

def bfs(M, N, board):

	answer = 0
	dirr = [[1, 0],[-1, 0],[0, 1], [0, -1]]
	check = [[0 for _ in range(M)] for _ in range(N)]

	for y in range(N):
		for x in range(M):
			if check[y][x] == 0 and board[y][x] == 1:
				q = deque()

				q.append((y, x))

				while q:
					yy, xx = q.popleft()

					for ydir, xdir in dirr:
						yyy = yy + ydir
						xxx = xx + xdir

						if 0 <= yyy < N and 0 <= xxx < M \
							and check[yyy][xxx] == 0 \
							and board[yyy][xxx] == 1:
							q.append((yyy,xxx))
							check[yyy][xxx] = 1

				answer += 1

	return answer

T = int(sys.stdin.readline())

for _ in range(T):
	M, N, K = map(int, sys.stdin.readline().split())

	board = [[0 for _ in range(M)] for _ in range(N)]

	for _ in range(K):
		X, Y = map(int, sys.stdin.readline().split())
		board[Y][X] = 1

	print(bfs(M, N, board))