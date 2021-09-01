import sys
import heapq

INF = 987654321

N, E = map(int, input().split())

board =[[] for _ in range(N)]

for _ in range(E):
	a, b, c = map(int, sys.stdin.readline().strip().split())
	board[a-1].append([b-1, c])
	board[b-1].append([a-1, c])

v1, v2 = map(int, sys.stdin.readline().strip().split())

def dijkstra(start, end):
	distance = [ INF for _ in range(N) ]

	distance[start] = 0
	queue = []
	heapq.heappush(queue, [0, start])

	while queue:
		d, v = heapq.heappop(queue)

		for nv, nd in board[v]:
			dd = d + nd
			if dd < distance[nv]:
				distance[nv] = dd
				heapq.heappush(queue, [dd, nv])

	return distance[end]

origin_to_v1 = dijkstra(0, v1-1)
origin_to_v2 = dijkstra(0, v2-1)

v1_to_v2 = dijkstra(v1-1, v2-1)
v2_to_v1 = dijkstra(v2-1, v1-1)

v1_to_N = dijkstra(v1-1, N-1)
v2_to_N = dijkstra(v2-1, N-1)

otoNv1 = origin_to_v1 + v1_to_v2 + v2_to_N
otoNv2 = origin_to_v2 + v2_to_v1 + v1_to_N

if otoNv1 >= INF and otoNv2 >= INF:
	print(-1)
elif otoNv1 >= INF and otoNv2 < INF:
	print(otoNv2)
elif otoNv1 < INF and otoNv2 >= INF:
	print(otoNv1)
else:
	if otoNv1 < otoNv2:
		print(otoNv1)
	else:
		print(otoNv2)