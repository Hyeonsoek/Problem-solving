import copy
from collections import deque

early_board = [ list(map(int, input().split())) for _ in range(3) ]

def find_zero(board):

	for y in range(3):
		for x in range(3):
			if board[y][x] == 0:
				return y, x

	return -1, -1

def board_correct(board):

	answer = [[1, 2, 3],
			[4, 5, 6],
			[7, 8, 0]]

	for y in range(3):
		if answer[y] != board[y]:
			return False

	return True

def _2DarrayToString(board):
	ret = ''

	for y in board:
		ret += ''.join(list(map(str, y)))

	return ret

def bfs():

	dirr = [[0, 1], [0, -1], [1, 0], [-1, 0]]
	q = deque()
	y, x = find_zero(early_board)

	check = {_2DarrayToString(early_board) : 1}

	q.append((0, y, x, early_board))

	while q:
		cost, y, x, board = q.popleft()

		if board_correct(board):
			return cost

		for ydir, xdir in dirr:
			yy = y + ydir
			xx = x + xdir
			if 0 <= yy < 3 and 0 <= xx < 3:
				board[yy][xx], board[y][x] = board[y][x], board[yy][xx]
				string_board = _2DarrayToString(board)

				if string_board not in check:
					check[string_board] = 1
					q.append((cost+1, yy, xx, copy.deepcopy(board)))

				board[yy][xx], board[y][x] = board[y][x], board[yy][xx]

	return -1

print(bfs())