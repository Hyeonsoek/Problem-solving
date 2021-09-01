def change_direction(face, clock_dict):

	for y in range(3):
		for x in range(3):
			for idx in range(len(face[y][x])):
				_, direction = face[y][x][idx]
				if direction in clock_dict:
					face[y][x][idx][1] = clock_dict[direction]

	return face


def LRrotate(cube, command):
	unclock = {'u':'b', 'b':'d', 'd':'f', 'f':'u'}
	clock = {'u':'f', 'f':'d', 'd':'b', 'b':'u'}
	
	face = [[0] * 3 for _ in range(3)]
	loc = -2

	if command in ['L+', 'R-']:
		loc = 0 if 'L' == command[0] else -1

		for z in range(3):
			for y in range(3):
				face[y][2 - z] = cube[z][y][loc]

		face = change_direction(face, clock)
	else :
		loc = 0 if 'L' == command[0] else -1
		
		for z in range(3):
			for y in range(3):
				face[2 - y][z] = cube[z][y][loc]

		face = change_direction(face, unclock)

	for z in range(3):
		for y in range(3):
			cube[z][y][loc] = face[z][y]

	return cube


def UDrotate(cube, command):
	unclock = {'f':'r', 'r':'b', 'b':'l', 'l':'f'}
	clock = {'f':'l', 'l':'b', 'b':'r', 'r':'f'}
	
	face = [[0] * 3 for _ in range(3)]
	loc = -2

	if command in ['D-', 'U+']:
		loc = 0 if 'U' == command[0] else -1

		for y in range(3):
			for x in range(3):
				face[x][2 - y] = cube[loc][y][x]

		face = change_direction(face, clock)
	else :
		loc = 0 if 'U' == command[0] else -1
		
		for y in range(3):
			for x in range(3):
				face[2 - x][y] = cube[loc][y][x]

		face = change_direction(face, unclock)

	for y in range(3):
		for x in range(3):
			cube[loc][y][x] = face[y][x]

	return cube

def FBrotate(cube, command):
	unclock = {'u':'l', 'l':'d', 'd':'r', 'r':'u'}
	clock = {'u':'r', 'r':'d', 'd':'l', 'l':'u'}
	
	face = [[0] * 3 for _ in range(3)]
	loc = -2

	if command in ['F+', 'B-']:
		loc = 0 if 'B' == command[0] else -1

		for z in range(3):
			for x in range(3):
				face[x][2 - z] = cube[z][loc][x]

		face = change_direction(face, clock)
	else :
		loc = 0 if 'B' == command[0] else -1
		
		for z in range(3):
			for x in range(3):
				face[2 - x][z] = cube[z][loc][x]

		face = change_direction(face, unclock)

	for z in range(3):
		for x in range(3):
			cube[z][loc][x] = face[z][x]

	return cube



def cubing():
	# 새 큐브 만들기 3x3x3
	cube = [[[[] for _ in range(3) ] \
				for _ in range(3) ] \
				for _ in range(3) ]

	for y in range(3):
		for x in range(3):
			cube[0][y][x].append(['w','u'])
			cube[-1][y][x].append(['y','d'])

	for z in range(3):
		for y in range(3):
			cube[z][y][0].append(['g','l'])
			cube[z][y][-1].append(['b','r'])

	for z in range(3):
		for x in range(3):
			cube[z][0][x].append(['o','b'])
			cube[z][-1][x].append(['r','f'])

	# 3개의 겹치는 경우의 수로 나누기
	LRcase = ['L-', 'L+', 'R-', 'R+']
	UDcase = ['U+', 'U-', 'D+', 'D-']
	FBcase = ['F+', 'F-', 'B+', 'B-']

	N = int(input())

	for command in input().split():
		if command in LRcase:
			cube = LRrotate(cube, command)
		if command in UDcase:
			cube = UDrotate(cube, command)
		if command in FBcase:
			cube = FBrotate(cube, command)

	for y in range(3):
		for x in range(3):
			for color, dit in cube[0][y][x]:
				if dit == 'u':
					print(color, end='')
					break
		print()

for _ in range(int(input())):
	cubing()