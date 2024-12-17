import sys

from collections import deque

def bfs(n):

	global check

	q = deque([1])
	check[1] = ['1', -1]

	while q:
		value = q.popleft()

		if value == 0:
			break

		for post in [0, 1]:
			vv = (value*10 + post) % n
			if check[vv] == ['', 0]:
				check[vv] = [str(post), value]
				q.append(vv)

def make_number(idx):
	global answer

	if idx == -1:
		return
	make_number(check[idx][1])
	answer += check[idx][0]

t = int(input())

for _ in range(t):
	answer = ''

	n = sys.stdin.readline().strip()

	check = [['', 0] for _ in range(int(n))]

	if n.count('0') + n.count('1') == len(n):
		print(n)
	else:
		bfs(int(n))
		make_number(0)
		print(answer)
