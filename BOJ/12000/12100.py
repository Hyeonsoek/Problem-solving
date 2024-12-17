def backtrack(ntime, board):
	if ntime == 5:
		return get_max_value(board)
	else:
		max_value = -1

		for repeat in range(4):
			board = rotate_board(board, repeat)
			max_value = max(max_value, backtrack(ntime+1, left_shift(board)))
			board = rotate_board(board, 4-repeat)

		return max_value

def left_shift(board):

	bboard = [ [x for x in y] for y in board ]

	for y in range(N):
		cnt = 0
		while 0 in bboard[y]:
			bboard[y].remove(0)
			cnt += 1

		for _ in range(cnt):
			bboard[y].append(0)

	for y in range(N):
		for x in range(N-1):
			if bboard[y][x] == bboard[y][x+1]:
				bboard[y][x] *= 2
				del bboard[y][x+1]
				bboard[y].append(0)
				
	return bboard

def get_max_value(board):

	max_value = -1

	for y in board:
		for x in y:
			if max_value < x:
				max_value = x

	return max_value

def rotate_board(board, n):

	bboard = [[board[N-1-x][y] for x in range(N)] for y in range(N)]

	if n > 1:
		bboard = rotate_board(bboard, n-1)

	return bboard


N = int(input())
BOARD = [ list(map(int, input().split())) for _ in range(N) ]

print(backtrack(0, BOARD))