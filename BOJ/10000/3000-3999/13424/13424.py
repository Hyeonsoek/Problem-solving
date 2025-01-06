import sys, heapq
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    k = int(input())
    target = list(map(int, input().split()))
    
    distance = [[sys.maxsize] * (n + 1) for _ in range(k)]
    for x in range(k):
        queue = [(0, target[x])]
        distance[x][target[x]] = 0
        while queue:
            dist, vertex = heapq.heappop(queue)
            
            if dist > distance[x][vertex]:
                continue
            
            for nbr, nbrdist in graph[vertex]:
                nextdist = dist + nbrdist
                if nextdist < distance[x][nbr]:
                    distance[x][nbr] = nextdist
                    heapq.heappush(queue, (nextdist, nbr))
    
    mindist = sys.maxsize
    result = 0
    for x in range(1, n + 1):
        distsum = sum([ distance[xx][x] for xx in range(k) ])
        if mindist > distsum:
            mindist = distsum
            result = x
        
    print(result)

t = int(input())
for _ in range(t):
    solve()