import sys
from itertools import permutations

# rotate board
def rotate_board(r, c, s, BOARD):

	r, c = r-1, c-1
	board = [ [y for y in x] for x in BOARD ]

	for ss in range(1, s+1):

		temp = []
			
		for cc in range(c - ss, c + ss + 1):
			temp.append(board[r-ss][cc])

		for rr in range(r - ss + 1, r + ss + 1):
			temp.append(board[rr][c + ss])

		for cc in range(c + ss - 1, c - ss - 1, -1):
			temp.append(board[r+ss][cc])

		for rr in range(r + ss - 1, r - ss, -1):
			temp.append(board[rr][c - ss])

		index = 0
		temp = temp[-1:] + temp[:-1]
		
		for cc in range(c - ss, c + ss + 1):
			board[r-ss][cc] = temp[index]
			index += 1

		for rr in range(r - ss + 1, r + ss + 1):
			board[rr][c + ss] = temp[index]
			index += 1

		for cc in range(c + ss - 1, c - ss - 1, -1):
			board[r+ss][cc] = temp[index]
			index += 1

		for rr in range(r + ss - 1, r - ss, -1):
			board[rr][c - ss] = temp[index]
			index += 1

	return board

# calculate matrix value
def calculate_matrix(BOARD):
	return min(list(map(sum, BOARD)))

# input line
N, M, K = map(int, sys.stdin.readline().split())
BOARD = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
operations = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]

answer = 987654321
op_order_list = list(permutations(operations))

for order in op_order_list:
	temp = rotate_board(*order[0], BOARD)
	for idx in range(1, len(order)):
		temp = rotate_board(*order[idx], temp)
	answer = min(answer, calculate_matrix(temp))

print(answer)