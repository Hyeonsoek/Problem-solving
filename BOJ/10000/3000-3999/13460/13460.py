from collections import deque

def is_in_board(y, x):
	return 0 <= y < N and 0 <= x < M

def move_to_wall(ydir, xdir, y, x):

	cost = 0
	yy, xx = y + ydir, x + xdir

	while is_in_board(yy, xx) and \
			board[yy][xx] != '#' and board[y][x] != 'O':
		y, x = yy, xx
		yy, xx = yy + ydir, xx + xdir
		cost += 1

	return y, x, cost

def bfs():
	check = set()
	q = deque()
	
	q.append((1, *rpoint, *bpoint))
	check.add((*rpoint, *bpoint))

	while q:
		cost, ry, rx, by, bx = q.popleft()

		if cost > 10:
			break

		for ydir, xdir in dirr:
			ryy, rxx, rcost = move_to_wall(ydir, xdir, ry, rx)
			byy, bxx, bcost = move_to_wall(ydir, xdir, by, bx)

			if board[byy][bxx] != 'O':
				if board[ryy][rxx] == 'O':
					return cost
				else :
					if (byy, bxx) == (ryy, rxx):
						if rcost > bcost:
							ryy, rxx = ryy - ydir, rxx - xdir
						else:
							byy, bxx = byy - ydir, bxx - xdir

					if (ryy, rxx, byy, bxx) not in check:
						q.append((cost+1, ryy, rxx, byy, bxx))
						check.add((ryy, rxx, byy, bxx))

	return -1



N, M = map(int, input().split())

board = [ list(input()) for _ in range(N) ]
dirr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

rpoint, bpoint = None, None
hole_point = None

for y in range(N):
	for x in range(M):
		if board[y][x] == 'R':
			rpoint = (y, x)
		if board[y][x] == 'B':
			bpoint = (y, x)
		if board[y][x] == 'O':
			hole_point = (y, x)

		if board[y][x] in ['R', 'B']:
			board[y][x] = '.'

print(bfs())