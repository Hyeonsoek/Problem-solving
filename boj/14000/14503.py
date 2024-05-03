N, M = map(int, input().split())
r, c, d = map(int, input().split())

mapp = [ list(map(int, input().split())) for _ in range(N) ]

drt = [(0, -1), (-1, 0), (0, 1), (1, 0)]
back = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def check():
	global mapp

	for y in mapp:
		for x in y:
			if x == 0:
				return False
	return True

def dir_change():
	global d

	d = d - 1 if d - 1 >= 0 else 3

def range_check(r, c):
	global N, M
	return 0 <= r < N and 0 <= c < M

def rlud_check(r, c):
	global N, M, mapp, drt

	for rdir, cdir in drt:
		rr = r + rdir
		cc = c + cdir

		if range_check(rr, cc) and mapp[rr][cc] == 0:
			return False

	return True

def cleanning():

	answer = 0
	dir_stack = 0

	global N, M, r, c, d, mapp, drt, back

	while not check():

		if mapp[r][c] == 0:
			mapp[r][c] = 2
			answer += 1
		else:
			if rlud_check(r, c):
				rr, cc = r + back[d][0], c + back[d][1]

				if not range_check(rr, cc):
					break
				if mapp[rr][cc] == 1:
					break

				r, c = rr, cc
				continue

			rr, cc = r + drt[d][0], c + drt[d][1]

			if range_check(rr, cc) and mapp[rr][cc] == 0:
				r, c = rr, cc
				dir_change()
				continue

			if (not range_check(rr, cc)) or \
					(range_check(rr, cc) and mapp[rr][cc] != 0):
				dir_change()

	return answer

print(cleanning())