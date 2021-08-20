import sys

from collections import deque
from collections import defaultdict

def bfs(n):

	global parent

	q = deque()
	check = [0] * n

	q.append( 1 )
	parent[1] = [-1, '1']

	while q:
		k = q.popleft()
		check[k] = 1

		if k == 0:
			break

		k_zero = (k * 10) % n
		k_one = (k * 10 + 1) % n

		if check[k_zero] == 0:
			parent[k_zero] = [k, '0']
			q.append( k_zero )
		if check[k_one] == 0:
			parent[k_one] = [k, '1']
			q.append( k_one )

def get_path(idx):
	global answer
	if idx == -1:
		return
	get_path(parent[idx][0])
	answer += parent[idx][1]

answer = []
t = int(input())

for _ in range(t):
	n = int(sys.stdin.readline().strip())

	if n == 1:
		print(1)
		continue

	parent = [[-1, '-1'] for _ in range(n)]
	bfs(n)

	answer = ''
	get_path(0)
	print(answer if answer != '-1' else "BRAK")