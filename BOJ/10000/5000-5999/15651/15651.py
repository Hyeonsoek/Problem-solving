from itertools import combinations as CB
from itertools import product as PD

N, M = map(int, input().split())

cb = list(CB(range(1, N+1), M))
result = []

for x in cb:
	pd = list(PD(x, repeat=M))
	for y in pd:
		result.append(y)
		
result = list(set(result))
result = sorted(result)

for x in result:
	print(*x)