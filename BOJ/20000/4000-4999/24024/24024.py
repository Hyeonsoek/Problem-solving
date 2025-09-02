import sys
import heapq
input = sys.stdin.readline

def solve():
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w, p = map(int, input().split())
        graph[u].append((v, w, p))
        graph[v].append((u, w, p))

    def dijkstra(r):
        distance = [float('inf') for _ in range(n+1)]
        distance[1] = 0
        pq = [(0, 1)]

        while pq:
            dist, node = heapq.heappop(pq)

            if dist > distance[node]:
                continue

            for neighbor, weight, color in graph[node]:
                nweight = weight + dist
                match color:
                    case 1: nweight += r
                    case 2: nweight += x - r
                if distance[neighbor] > nweight:
                    distance[neighbor] = nweight
                    heapq.heappush(pq, (nweight, neighbor))

        return distance[n]

    s = 0; e = x
    while s < e:
        left = (2 * s + e) // 3
        right = (s + 2 * e) // 3

        left_dist = dijkstra(left)
        right_dist = dijkstra(right)

        if left_dist <= right_dist:
            s = left + 1
        else:
            e = right - 1

    maxValue = 0
    for i in range(max(s - 2, 0), min(e + 2, x) + 1):
        maxValue = max(maxValue, dijkstra(i))

    print(maxValue)

solve()