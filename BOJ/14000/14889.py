from itertools import combinations

def min_stat_gap():
	number = [x for x in range(N)]
	number_combi = list(combinations(number, N//2))

	min_stat = 987654321

	for group1 in number_combi:
		group2 = list(set(number) - set(group1))
		group1 = list(group1)
		min_stat = min(min_stat, abs(get_stat(group1) - get_stat(group2)))

	return min_stat

def get_stat(group):

	stat = 0

	for y in group:
		for x in group:
			stat += board[y][x]

	return stat


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(min_stat_gap())