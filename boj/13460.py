## 2021/08/03 아직 못풀었음

from collections import deque

N, M = map(int, input().split())

board = [ list(input()) for _ in range(N) ]
dirr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

color_opp = {'R':'B', 'B':'R'}

Rpoint, Bpoint = None, None
Hole_point = None

for y in range(N):
	for x in range(M):
		if board[y][x] == 'R':
			Rpoint = (y, x)
		if board[y][x] == 'B':
			Bpoint = (y, x)
		if board[y][x] == 'O':
			Hole_point = (y, x)

		if board[y][x] in ['R', 'B', 'O']:
			board[y][x] = '.'

def is_in_board(y, x):
	global N, M
	return 0 <= y < N and 0 <= x < M

def can_hole_in_two_ball(ry, rx, by, bx):

	global dirr
		
	if not (ry == by or rx == bx):
		return False

	count = 0

	for ydir, xdir in dirr:
		ryy, rxx = ry, rx
		byy, bxx = by, bx

		red_meet_O, blue_meet_O = False, False
		red_plus, blue_plus = True, True

		while (is_in_board(ryy, rxx) and is_in_board(byy, bxx)) and \
					(red_plus or blue_plus):

			if (byy, bxx) == Hole_point:
				blue_meet_O = True
				blue_plus = False

			if (ryy, rxx) == Hole_point:
				red_meet_O = True
				red_plus = False

			if red_plus:
				ryy += ydir
				rxx += xdir

			if blue_plus:
				byy += ydir
				bxx += xdir

			if not (is_in_board(ryy, rxx) and is_in_board(byy, bxx)):
				break

			if board[ryy][rxx] == '#' and red_plus:
				ryy -= ydir
				rxx -= xdir
				red_plus = False

			if board[byy][bxx] == '#' and blue_plus:
				byy -= ydir
				bxx -= xdir
				blue_plus = False

		if red_meet_O == True:
			if blue_meet_O == True:
				return True
			return False

	return False


def can_hole_in_one_ball(y, x, other):

	global dirr, Hole_point, board

	for ydir, xdir in dirr:
		yy = y
		xx = x
		while is_in_board(yy, xx) and board[yy][xx] != '#' and \
				(yy, xx) != other:
			if (yy, xx) == Hole_point:
				return True
			yy += ydir
			xx += xdir

	return False


# 여기서 O에 들어가는 경우의 수를 걸러줘야함
def get_coordi_next_wall(ydir, xdir, rpoint, bpoint):

	ryy, rxx = rpoint[0], rpoint[1]
	byy, bxx = bpoint[0], bpoint[1]

	red_plus, blue_plus = True, True

	# print('STATR : ', ryy, rxx, byy, bxx)

	while (is_in_board(ryy, rxx) and is_in_board(byy, bxx)) and \
				(red_plus or blue_plus):

		# print('1 : ',ryy, rxx, byy, bxx)

		if (ryy, rxx) == Hole_point or (byy, bxx) == Hole_point:
			return None

		if red_plus:
			ryy += ydir
			rxx += xdir

		if blue_plus:
			byy += ydir
			bxx += xdir

		# print('2 : ',ryy, rxx, byy, bxx)

		if not (is_in_board(ryy, rxx) and is_in_board(byy, bxx)):
			break

		if (board[ryy][rxx] == '#' and board[byy][bxx] == '#') or\
			(board[ryy][rxx] == '#' and (byy + ydir, bxx + xdir) == (ryy, rxx)) or\
			(board[byy][bxx] == '#' and (ryy + ydir, rxx + xdir) == (byy, bxx)):
			ryy -= ydir
			rxx -= xdir
			byy -= ydir
			bxx -= xdir
			break

		if (board[ryy][rxx] == '#' or (ryy, rxx) == (byy, bxx)) and red_plus:
			ryy -= ydir
			rxx -= xdir
			red_plus = False

		# print('3 : ',ryy, rxx, byy, bxx)

		if (board[byy][bxx] == '#' or (ryy, rxx) == (byy, bxx)) and blue_plus:
			byy -= ydir
			bxx -= xdir
			blue_plus = False

		# print('4 : ',ryy, rxx, byy, bxx)

		# print("-------------------------")

	return ryy, rxx, byy, bxx

def bfs():

	global N, M, board, dirr

	q = deque()
	check = set()

	q.append((0, *Rpoint, *Bpoint))
	check.add((*Rpoint, *Bpoint))

	# ryy, rxx, byy, bxx = get_coordi_next_wall(*dirr[1], Rpoint, Bpoint)

	while q:
		cost, ry, rx, by, bx = q.popleft()

		print('START : ', ry, rx, by, bx)

		#print('TWO BALL')
		if can_hole_in_two_ball(ry, rx, by, bx):
			continue
		#print('ONE BALL')
		if can_hole_in_one_ball(ry, rx, (by, bx)):
			return cost+1

		for ydir, xdir in dirr:
			# print("---------START--------")
			coordinate = get_coordi_next_wall(ydir, xdir, (ry, rx), (by, bx))
			# print("--------END--------")

			if coordinate is not None and coordinate not in check:
				print("\t", *coordinate)
				q.append((cost+1, *coordinate))
				check.add(coordinate)

	return -1


answer = bfs()

if answer > 10:
	print(-1)
else:
	print(answer)