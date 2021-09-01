import sys

N = int(sys.stdin.readline())
S = set()

for _ in range(N):
	inn = sys.stdin.readline().split()

	if inn[0] == 'add':
		S.add(int(inn[1]))
	if inn[0] == 'remove':
		if int(inn[1]) in S:
			S.remove(int(inn[1]))
	if inn[0] == 'check':
		if int(inn[1]) in S:
			print(1)
		else:
			print(0)
	if inn[0] == 'toggle':
		if int(inn[1]) in S:
			S.remove(int(inn[1]))
		else:
			S.add(int(inn[1]))
	if inn[0] == 'all':
		S = set(range(1, 21))
	if inn[0] == 'empty':
		S.clear()