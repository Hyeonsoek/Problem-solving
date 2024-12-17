def get_line_count():
	cnt = 0
	for idx in range(N):
		if is_line(board[idx]):
			cnt += 1
		if is_line(rotate_board[idx]):
			cnt += 1
	return cnt

def is_line(line):

	global N, L

	if sum(line) == N * max(line):
		return True

	for x in range(N-1):
		if not (line[x] - 1 <= line[x+1] <= line[x] + 1):
			return False

	check = [0] * N

	x = 0
	while x < N-1:
		if line[x] == line[x+1] + 1 \
				and sum(line[x+1:x+L+1]) == line[x+1] * L \
				and ((x + L + 1 < N and line[x+1] != line[x+L+1]-1) or x + L + 1 == N):
			for i in range(x+1, x+L+1):
				check[i] = 1
			x += L
			continue
		if line[x] in [line[x+1], line[x+1]-1]:
			x += 1
			continue
		return False

	x = N-1
	while x > 0:
		if sum(check[x-L:x]) == 0 \
				and line[x] == line[x-1] + 1 \
				and sum(line[x-L:x]) == line[x-1] * L \
				and ((x >= L + 1 and line[x-1] != line[x-L-1]-1) or x == L):
			x -= L
			continue
		if line[x] in [line[x-1], line[x-1]-1]:
			x -= 1
			continue
		return False

	return True

N, L = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
rotate_board = list(map(list, zip(*board)))

print(get_line_count())