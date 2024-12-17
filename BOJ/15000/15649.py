from itertools import combinations as CB
from itertools import permutations as PM

N, M = map(int, input().split())

cb = list(CB(range(1, N+1), M))
result = []

for x in cb:
	pm = list(PM(x))
	for y in pm:
		result.append(y)

result = sorted(result)

for x in result:
	print(*x)