import sys
from collections import deque

def bipartite_graph(V, E, board):

	answer = 0
	check = [ 0 for _ in range(V) ]

	for start in range(V):
		if check[start] == 0:
			q = deque()
			check[start] = 1
			q.append((start, 1))

			while q:
				v, value = q.popleft()

				for xx in board[v]:
					if check[xx] == 0:
						check[xx] = -value
						q.append((xx,-value))
					elif check[xx] == check[v]:
						return False
	return True

T = int(sys.stdin.readline())

for _ in range(T):
	V, E = map(int, sys.stdin.readline().split())

	board = [[] for _ in range(V)]

	for _ in range(E):
		s, e = map(int, sys.stdin.readline().split())

		board[s-1].append(e-1)
		board[e-1].append(s-1)

	print('YES' if bipartite_graph(V, E, board) else 'NO')