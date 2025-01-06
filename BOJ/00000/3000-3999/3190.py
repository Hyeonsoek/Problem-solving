N = int(input())
K = int(input())

board = [ [0] * N for _ in range(N) ]
apple = [ tuple(map(int, input().split())) for _ in range(K) ]

L = int(input())

redir = [ input().split() for _ in range(L) ]

for y, x in apple:
	board[y-1][x-1] = 1

now, d = 0, 1
body = [(0, 0)] # tail = 0, haed = -1

LEFT = [3, 0, 1, 2]
RIGHT = [1, 2, 3, 0]
DRT = [[-1, 0], [0, 1], [1, 0], [0, -1]] #direction

while True:

	if len(redir) > 0 and now == int(redir[0][0]):
		if redir[0][1] == 'L':
			d = LEFT[d]
		if redir[0][1] == 'D':
			d = RIGHT[d]

		del redir[0]

	now += 1
	head_r, head_c = body[-1]
	rr, cc = head_r + DRT[d][0], head_c + DRT[d][1]

	if 0 <= rr < N and 0 <= cc < N:
		if (rr, cc) in body:
			break

		if board[rr][cc] == 1:
			board[rr][cc] = 0
		else :
			del body[0]
		body.append((rr, cc))
	else :
		break

print(now)