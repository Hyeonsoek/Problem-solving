import sys

from collections import deque

dirr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
left = [3, 0, 1, 2]
right = [1, 2, 3, 0]

w, h = map(int, input().split())
board = [list(sys.stdin.readline().strip()) for _ in range(h)]

def bfs(sy, sx):

	q = deque()
	check = [[0] * w for _ in range(h)]

	def can_append(y, x):
		return 0 <= y < h and 0 <= x < w \
				and check[y][x] == 0 \
				and board[y][x] != '*'

	answer = 987654321
	check[sy][sx] = 1

	for idx, dd in enumerate(dirr):
		ydir, xdir = dd
		yy, xx = sy + ydir, sx + xdir
		if 0 <= yy < h and 0 <= xx < w:
			if board[yy][xx] == '*':
				continue
			if board[yy][xx] == 'C':
				return 0
			q.append((yy, xx, idx, 0))

	while q:
		y, x, d, cost = q.popleft()
		check[y][x] = 1

		# print(y, x, d)

		if board[y][x] == 'C':
			if answer > cost:
				answer = cost
			continue

		lydir, lxdir = dirr[left[d]]
		ly, lx = y + lydir, x + lxdir

		# print('\t', ly, lx)

		if can_append(ly, lx):
			q.append((ly, lx, left[d], cost+1))

		rydir, rxdir = dirr[right[d]]
		ry, rx = y + rydir, x + rxdir

		# print('\t', ry, rx)

		if can_append(ry, rx):
			q.append((ry, rx, right[d], cost+1))

		stydir, stxdir = dirr[d] #straight
		sty, stx = y + stydir, x + stxdir

		# print('\t', sty, stx)

		if can_append(sty, stx):
			q.appendleft((sty, stx, d, cost))

	return answer

def get_start_coordinate():
	for y in range(h):
		for x in range(w):
			if board[y][x] == 'C':
				return (y, x)
	return (-1, -1)

print(bfs(*get_start_coordinate()))