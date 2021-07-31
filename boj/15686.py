from itertools import combinations

N, M = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(N)]

housese = []
chickens = []

for y in range(N):
	for x in range(N):
		if info[y][x] == 1:
			housese.append((y,x))
		if info[y][x] == 2:
			chickens.append((y,x))

def get_distance(loc1, loc2):
	return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])

def find_min_distance_chicken():

	global N, M, info, housese, chickens

	answer = 987654321

	for locs in list(combinations(chickens, M)):
		distance = 0
		for house in housese:
			house_min = 987654321
			for loc in locs:
				house_min = min(house_min, get_distance(loc, house))
			distance += house_min

		answer = min(distance, answer)

	return answer

print(find_min_distance_chicken())