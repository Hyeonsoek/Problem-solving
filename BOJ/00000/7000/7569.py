from collections import deque

M, N, H = input().split()
M, N, H = int(M), int(N), int(H)

board = [[[int(x) for x in input().split()] \
			for y in range(N)]\
				for z in range(H)]

DIRR = [[0,0,-1],[0,0,1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]

def bfs():

	global M, N, H, board, DIRR

	pq = deque()
	days = -1

	for z in range(H):
		for y in range(N):
			for x in range(M):
				if board[z][y][x] == 1:
					pq.append((x,y,z,0))

	while pq:
		x, y, z, day = pq.popleft()

		if day > days:
			days = day

		for xdir, ydir, zdir in DIRR:
			xx = x + xdir
			yy = y + ydir
			zz = z + zdir

			if 0 <= xx < M and 0 <= yy < N and 0 <= zz < H and \
					board[zz][yy][xx] == 0:
				board[zz][yy][xx] = 1
				pq.append((xx, yy, zz, day+1))

	for z in board:
		for y in z:
			for x in y:
				if x == 0:
					return -1

	return days

print(bfs())