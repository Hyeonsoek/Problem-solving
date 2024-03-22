import sys
import heapq
INF = 10000000000
input = sys.stdin.readline

def dijkstra(graph, start, n):
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0

    queue = [(0, start)]
    while queue:
        dist, node = heapq.heappop(queue)

        for nbr, weight in graph[node]:
            nbrDist = dist + weight
            if nbrDist < distance[nbr]:
                distance[nbr] = nbrDist
                heapq.heappush(queue, (nbrDist, nbr))

    return distance

def solve():
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for x in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    cadidates = [int(input()) for _ in range(t)]

    distance_s = dijkstra(graph, s, n)
    distance_g = dijkstra(graph, g, n)
    distance_h = dijkstra(graph, h, n)

    result = []
    for x in cadidates:
        sg = distance_s[g]
        gh = distance_g[h]
        hx = distance_h[x]

        sh = distance_s[h]
        hg = distance_h[g]
        gx = distance_g[x]

        if distance_s[x] == sg + gh + hx or distance_s[x] == sh + hg + gx:
            result.append(x)

    print(*sorted(result))

t = int(input())
for _ in range(t):
    solve()