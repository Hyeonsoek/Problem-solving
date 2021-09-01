import sys
import heapq

INF = 10 ** 9

# 정직하게 매트릭스 짜서 넣는 식으로 함
# 대신에 최솟값 업데이트를 계속 해주는 방향임
# 해당 문제에서는 입력으로 들어오는 간선 비용이
# 여러개라서 이렇게 해야함

def dijkstra(start, end):

	queue = []
	cost = [INF for _ in range(N)]

	cost[start] = 0
	heapq.heappush(queue, [0, start])

	while queue:
		c, vertex = heapq.heappop(queue)

		for vv in range(N):
			if  board[vertex][vv] != -1 \
					and c + board[vertex][vv] < cost[vv]:
				cost[vv] = c + board[vertex][vv]
				heapq.heappush(queue, [cost[vv], vv])

	return cost[end]

N = int(input())
M = int(input())

board = [[-1] * N for _ in range(N)]

for _ in range(M):
	a, b, c = map(int, sys.stdin.readline().strip().split())
	if board[a-1][b-1] == -1 or board[a-1][b-1] > c:
		board[a-1][b-1] = c

start, end = map(int, sys.stdin.readline().strip().split())

print(dijkstra(start-1, end-1))