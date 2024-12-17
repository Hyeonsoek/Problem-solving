import sys, heapq
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start, end):
        dist = [float('inf') for _ in range(n + 1)]

        dist[start] = 0
        queue = [(0, start)]

        while queue:
            cost, curr = heapq.heappop(queue)

            if dist[curr] < cost:
                continue

            for dest, dest_cost in graph[curr]:
                next_cost = cost + dest_cost
                if next_cost < dist[dest]:
                    dist[dest] = next_cost
                    heapq.heappush(queue, (next_cost, dest))

        return dist[end]

    print(dijkstra(*map(int, input().split())))

solve()