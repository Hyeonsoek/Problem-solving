from itertools import combinations

def solution(n, weak, dist):
    answer = 0

    outer_wall = [ 0 for x in range(n) ]

    for w in weak:
    	outer_wall[w] = 1

    for l in range(len(dist)):
    	dist_comb = combinations(dist, l+1)

    	for comb in dist_comb:
    		print(comb)

    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))