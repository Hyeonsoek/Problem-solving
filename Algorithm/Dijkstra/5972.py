import sys, heapq
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        arr[start].append((end, cost))
        arr[end].append((start, cost))

    def dijkstra(start):
        dist = [1e9 for _ in range(n+1)]

        dist[start] = 0
        queue = [(0, start)]
        while queue:
            cost, curr = heapq.heappop(queue)

            if dist[curr] < cost:
                continue

            for dest, dest_cost in arr[curr]:
                next_cost = cost + dest_cost
                if dist[dest] > next_cost:
                    dist[dest] = next_cost
                    heapq.heappush(queue, (next_cost, dest))

        return dist[n]

    print(dijkstra(1))

solve()