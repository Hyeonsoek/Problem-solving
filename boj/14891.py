import copy

def rotate(gear, arrow):

	ret = copy.deepcopy(gear)

	if arrow == -1:
		ret.append(ret[0])
		del ret[0]
	else:
		ret.insert(0, ret[-1])
		ret.pop()

	return ret

def gear_rotate(gears, index, arrow):

	ret = copy.deepcopy(gears)

	now_arrow = arrow
	for idx in range(index, 3):
		if gears[idx+1][-2] != gears[idx][2]:
			ret[idx+1] = rotate(gears[idx+1], -now_arrow)
			now_arrow = -now_arrow
		else:
			break

	now_arrow = arrow
	for idx in range(index, 0, -1):
		if gears[idx][-2] != gears[idx-1][2]:
			ret[idx-1] = rotate(gears[idx-1], -now_arrow)
			now_arrow = -now_arrow
		else:
			break

	ret[index] = rotate(gears[index], arrow)

	return ret

gears = [list(input()) for _ in range(4)]

rotation = int(input())
for _ in range(rotation):
	index, arrow = map(int, input().split())
	gears = gear_rotate(gears, index-1, arrow)

answer = 0
for i in range(4):
	if gears[i][0] == '1':
		answer += 2**i

print(answer)