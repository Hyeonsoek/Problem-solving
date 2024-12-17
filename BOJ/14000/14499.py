
def move(d):

	global dice, y, x

	yy, xx = y + dirr[d][0], x + dirr[d][1]

	if not (0 <= yy < N and 0 <= xx < M):
		return None

	y, x = yy, xx
	bottom, top = dice[4], dice[1]

	if d in [0, 1]:

		left, right = dice[2], dice[3]

		if d == 1:
			left, bottom, right, top = bottom, right, top, left
		else :
			left, bottom, right, top = top, left, bottom, right

		dice[2], dice[3] = left, right

	else:

		front, back = dice[0], dice[5]

		if d == 3:
			back, bottom, front, top = bottom, front, top, back
		else :
			back, bottom, front, top = top, back, bottom, front

		dice[0], dice[5] = front, back

	dice[4], dice[1] = bottom, top

	if board[y][x] == 0:
		board[y][x] = bottom
	else :
		dice[4]= board[y][x]
		board[y][x] = 0

	return dice[1]

# 0 - front
# 1 - up
# 2 - right
# 3 - left
# 4 - down
# 5 - back

N, M, y, x, K = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
d_command = list(map(int, input().split()))

dirr = [[0, 1], [0, -1], [-1, 0], [1, 0]]
dice = [ 0 for _ in range(6) ]

for d in d_command:
	value = move(d-1)

	if value != None:
		print(value)