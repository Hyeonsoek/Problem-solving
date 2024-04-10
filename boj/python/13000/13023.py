import sys

N, M = map(int, input().split())

check = [ 0 for _ in range(N) ]
board = [ [] for _ in range(N) ]
relation = [ list(map(int, sys.stdin.readline().split())) for _ in range(M) ]

for y, x in relation:
	board[y].append(x)
	board[x].append(y)

def dfs(start, depth):

	global answer

	check[start] = 1

	if depth == 5:
		answer = 1
	else:
		for xx in board[start]:
			if check[xx] == 0:
				dfs(xx, depth + 1)
				check[xx] = 0

answer = 0
for x in range(N):
	dfs(x, 1)
	check = [ 0 for _ in range(N) ]
	if answer == 1:
		break

print(answer)