# 정공법 코드 - 시간초과 무적권남

import copy

N = int(input())

answer = 0
answer_board = []
board = [[0] * N for _ in range(N)]

def check(y, x):
	dirr = [[-1, -1], [1, 1], [-1, 1], [1, -1]]

	for ydir, xdir in dirr:
		yy, xx = y + ydir, x + xdir
		while 0 <= yy < N and 0 <= xx < N:
			if board[yy][xx] == 1:
				return False
			yy, xx = yy + ydir, xx + xdir

	for idx in range(N):
		if board[y][idx] == 1:
			return False
		if board[idx][x] == 1:
			return False

	return True

def Nqueen(idx, cnt):
	global answer
	y, x = idx//N, idx%N

	if (y, x) == (N-1, N-1):
		if cnt == N or (check(y, x) and cnt == N-1):
			answer += 1
	else :
		if check(y, x):
			board[y][x] = 1
			Nqueen(idx+1, cnt+1)
			board[y][x] = 0
		Nqueen(idx+1, cnt)

Nqueen(0, 0)
print(answer)