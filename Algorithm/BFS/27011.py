import sys
from collections import deque
input = sys.stdin.readline

n, dest = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    start, end = map(int, input().split())
    graph[start].append(end)
    
visited = [0] * (n + 1)
visited[1] = 1

queue = deque()
queue.append((1, [1]))

while queue:
    vertex, route = queue.popleft()
    
    if vertex == dest:
        print(len(route))
        for vv in route:
            print(vv)
        exit(0)
    
    for next in graph[vertex]:
        if not visited[next]:
            visited[next] = 1
            next_route = route[:] + [next]
            queue.append((next, next_route))
            
print(-1)