import sys
import copy

from collections import deque
from collections import defaultdict

def to_string(y, x):
	return str(y) + '/' + str(x)

def bfs():

	answer = 0
	pre_check = None
	key = defaultdict(int)
	docoment = defaultdict(int)

	dirr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
	make_check = lambda : [[-1] * (W+2) for _ in range(H+2)]

	while True:
		q = deque()
		check = make_check()

		q.append((0, 0))
		check[0][0] = 1

		while q:
			y, x = q.popleft()

			for ydir, xdir in dirr:
				yy = y + ydir
				xx = x + xdir
				if 0 <= yy < H+2 and 0 <= xx < W+2 \
						and board[yy][xx] != '*' and check[yy][xx] == -1:

					string = to_string(yy,xx)

					if ord('A') <= ord(board[yy][xx]) <= ord('Z') \
							and board[yy][xx].lower() in keys:
						q.append((yy, xx))
						check[yy][xx] = 1

					if ord('a') <= ord(board[yy][xx]) <= ord('z'):
						if key[string] == 0:
							key[string] = 1
							keys.append(board[yy][xx])
						check[yy][xx] = 1
						q.append((yy, xx))

					if board[yy][xx] == '.':
						check[yy][xx] = 1
						q.append((yy, xx))

					if board[yy][xx] == '$':
						if docoment[string] == 0:
							answer += 1
							docoment[string] = 1
						check[yy][xx] = 1
						q.append((yy, xx))

		if pre_check and pre_check == check:
			break

		pre_check = copy.deepcopy(check)

	return answer

answer = []
T = int(input())

for _ in range(T):
	H, W = map(int, input().split())
	board = [list('.' + sys.stdin.readline().strip() + '.') for _ in range(H)]
	keys = list(sys.stdin.readline().strip())

	board.insert(0, ['.'] * (W+2))
	board.append(['.'] * (W+2))

	answer.append(bfs())

for a in answer:
	print(a)