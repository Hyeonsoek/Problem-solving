def get_line_count():
	cnt = 0
	for idx in range(N):
		if is_line(board[idx]):
			cnt += 1
		if is_line(rotate_board[idx]):
			cnt += 1
	return cnt

def is_line(line):

	if sum(line) == int(len(line)) * line[0]:
		return True

	for x in range(N-1):
		if not (line[x] - 1 <= line[x+1] <= line[x] + 1):
			return False

	for x in range(N):



N, L = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
rotate_board = list(zip(*board))

print(get_line_count())