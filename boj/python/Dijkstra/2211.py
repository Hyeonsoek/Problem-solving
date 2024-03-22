import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, n, start=1):
    distance = [[float("inf"), []] for _ in range(n + 1)]
    distance[start][0] = 0

    queue = [(0, [], start)]
    while queue:
        dist, route, node = heapq.heappop(queue)

        for nbr, weight in graph[node]:
            nbrDistance = dist + weight
            if nbrDistance < distance[nbr][0]:
                route.append((node, nbr))
                distance[nbr][0] = nbrDistance
                distance[nbr][1] = route[:]
                heapq.heappush(queue, (nbrDistance, route[:], nbr))
                route.pop()

    return distance

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    distance = dijkstra(graph, n)
    result = set()
    for _, route in distance:
        for a, b in route:
            if (b, a) not in result:
                result.add((a, b))
    print(len(result))
    for a, b in result:
        print(a, b)

solve()