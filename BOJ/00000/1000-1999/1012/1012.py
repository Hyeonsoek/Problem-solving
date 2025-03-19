import sys
from collections import deque
input = sys.stdin.readline
DRX = [-1, 1, 0, 0]
DRY = [0, 0, -1, 1]

def solve(M, N, board):
	result = 0
	visited = [[0 for _ in range(M)] for _ in range(N)]

	def bfs(y, x):
		q = deque([(y, x)])

		while q:
			sy, sx = q.popleft()

			for i in range(4):
				ny = sy + DRY[i]
				nx = sx + DRX[i]

				if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and board[ny][nx]:
					q.append((ny, nx))
					visited[ny][nx] = 1

		return 1

	for y in range(N):
		for x in range(M):
			if not visited[y][x] and board[y][x]:
				result += bfs(y, x)

	return result

T = int(input())

for _ in range(T):
	M, N, K = map(int, input().split())
	board = [[0 for _ in range(M)] for _ in range(N)]
	for _ in range(K):
		X, Y = map(int, input().split())
		board[Y][X] = 1

	print(solve(M, N, board))