import sys, heapq
inf = float("inf")
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    wards = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start):
        dist = [inf] * n
        dist[start] = 0
        queue = [(0, start)]

        while queue:
            cost, curr = heapq.heappop(queue)

            if cost > dist[curr]:
                continue

            for dest, dest_cost in graph[curr]:
                next_cost = cost + dest_cost
                if (wards[dest] != 1 or dest == n - 1) and next_cost < dist[dest]:
                    dist[dest] = next_cost
                    heapq.heappush(queue, (next_cost, dest))

        return dist[n-1]

    result = dijkstra(0)
    print(-1 if result == inf else result)

solve()