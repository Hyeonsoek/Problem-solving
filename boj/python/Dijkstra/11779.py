import sys, heapq
inf = float("inf")
input = sys.stdin.readline

def solve():
    n, m = int(input()), int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))

    start, end = map(int, input().split())

    dist = [[inf, []] for _ in range(n+1)]
    dist[start][0] = 0
    queue = [(0, start, [start])]

    while queue:
        cost, curr, route = heapq.heappop(queue)

        if dist[curr][0] < cost:
            continue

        for dest, dest_cost in graph[curr]:
            next_cost = cost + dest_cost
            if next_cost < dist[dest][0]:
                dist[dest][0] = next_cost
                dist[dest][1] = route[:] + [dest]
                heapq.heappush(queue, (next_cost, dest, route[:] + [dest]))

    result, route = dist[end]
    print(result, len(route), sep='\n')
    print(*route)

solve()