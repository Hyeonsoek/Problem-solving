import sys, heapq
input = sys.stdin.readline

def dijkstra(start, v, graph):
    queue = [(0, start)]
    distance = [sys.maxsize] * (v + 1)
    distance[start] = 0
    
    while queue:
        dist, vertex = heapq.heappop(queue)
        
        if dist > distance[vertex]:
            continue
        
        for nbr, nbrdist in graph[vertex]:
            nextdist = dist + nbrdist
            if distance[nbr] > nextdist:
                distance[nbr] = nextdist
                heapq.heappush(queue, (nextdist, nbr))
    
    return distance

def solve():
    v, e, p = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for x in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    distance = dijkstra(1, v, graph)
    distance_p = dijkstra(p, v, graph)
    
    print("SAVE HIM" if distance[v] >= distance[p] + distance_p[v] else "GOOD BYE")

solve()