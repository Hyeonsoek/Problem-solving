import sys

from itertools import permutations
from collections import deque

MAX = 987654321
dirr = [[1, 0],[-1, 0], [0, 1], [0, -1]]

def check_unreachable():
	for y in sdt:
		if abs(sum(y)) == ldirty:
			return True
	return False

def bfs_board(sy, sx, ey, ex):

	q = deque()
	check = [[-1] * W for _ in range(H)]

	q.append((sy, sx))
	check[sy][sx] = 0

	while q:
		y, x = q.popleft()

		if (y, x) == (ey, ex):
			return check[y][x]

		for ydir, xdir in dirr:
			yy, xx = y + ydir, x + xdir
			if 0 <= yy < H and 0 <= xx < W \
					and check[yy][xx] == -1 \
					and board[yy][xx] != 'x':
				check[yy][xx] = check[y][x] + 1
				q.append((yy, xx))

	return -1

while True:
	W, H = map(int, sys.stdin.readline().split())

	if W == H == 0:
		break

	board = [list(sys.stdin.readline().strip()) for _ in range(H)]

	start = [-1, -1]
	dirty = []
	for y in range(H):
		for x in range(W):
			if board[y][x] == 'o':
				start = [y, x]
			if board[y][x] == '*':
				dirty.append([y, x])

	dirty.insert(0, start)

	ldirty = len(dirty)
	sdt = [[-1] * ldirty for _ in range(ldirty)]
	sdt_min = MAX

	for y in range(ldirty):
		for x in range(ldirty):
			if y != x:
				sdt[y][x] = bfs_board(*dirty[y], *dirty[x])

	if check_unreachable():
		print(-1)
		continue

	pt = list(permutations(list(range(ldirty-1))))

	for p in pt:
		start, cost = 0, 0
		for x in p:
			cost += sdt[start][x+1]
			start = x+1
		if cost < sdt_min:
			sdt_min = cost

	print(sdt_min)