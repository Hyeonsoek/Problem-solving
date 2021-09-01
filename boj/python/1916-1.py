import sys
import heapq

INF = 10 ** 9

#입력을 각 정점에서 연결된 정점과 비용으로 넣고 풀었더니
#해당 문제에는 간선이 여러개라서 비용이 최솟값으로 되있는게
#아니라서 더 큰값을 스킵시키는 방향으로 짠거

def dijkstra(start, end):

	queue = []
	cost = [INF for _ in range(N)]

	cost[start] = 0
	heapq.heappush(queue, [0, start])

	while queue:
		c, vertex = heapq.heappop(queue)

		if c > cost[vertex]:
			continue

		for vv, cc in board[vertex]:
			if c + cc < cost[vv]:
				cost[vv] = c + cc
				heapq.heappush(queue, [cost[vv], vv])

	return cost[end]

N = int(input())
M = int(input())

board = [[] for _ in range(N)]

for _ in range(M):
	a, b, c = map(int, sys.stdin.readline().strip().split())
	board[a-1].append([b-1, c])

start, end = map(int, sys.stdin.readline().strip().split())

print(dijkstra(start-1, end-1))