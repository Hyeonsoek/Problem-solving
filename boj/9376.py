import sys
from collections import deque

MAX = 987654321

T = int(input())

def bfs(sy, sx):

	q = deque()
	dirr = [[1, 0],[-1, 0],[0, 1],[0, -1]]
	distance = [[-1] * (W+2) for _ in range(H+2)]

	q.append((sy, sx))
	distance[sy][sx] = 0

	while q:
		y, x = q.popleft()

		for ydir, xdir in dirr:
			yy = y + ydir
			xx = x + xdir
			if 0 <= yy < H+2 and 0 <= xx < W+2 and distance[yy][xx] == -1:
				if board[yy][xx] in ['.', '$']:
					distance[yy][xx] = distance[y][x]
					q.appendleft((yy, xx))
				if board[yy][xx] == '#':
					distance[yy][xx] = distance[y][x] + 1
					q.append((yy, xx))

	return distance

for _ in range(T):
	H, W = map(int, sys.stdin.readline().split())
	board = [ list(('.' + sys.stdin.readline().strip() + '.')) for _ in range(H) ]

	board.insert(0, ['.'] * (W+2))
	board.append(['.'] * (W+2))

	prisoner = []
	for y in range(H+2):
		for x in range(W+2):
			if board[y][x] == '$':
				prisoner.append((y, x))

	dist_s = bfs(0, 0)
	dist_p1 = bfs(*prisoner[0])
	dist_p2 = bfs(*prisoner[1])

	answer = MAX

	for y in range(H+2):
		for x in range(W+2):
			if -1 not in [dist_s[y][x], dist_p1[y][x], dist_p2[y][x]]:
				result = dist_s[y][x] + dist_p1[y][x] + dist_p2[y][x]
				result -= 2 if board[y][x] == '#' else 0
				answer = min(answer, result)

	print(answer)