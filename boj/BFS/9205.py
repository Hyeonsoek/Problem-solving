import sys, collections
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    vertexes = [ tuple(map(int, input().split())) for _ in range(n + 2) ]
    graph = [ [0] * (n + 2) for _ in range(n + 2) ]
    
    for start in range(n + 1):
        for end in range(start + 1, n + 2):
            sx, sy = vertexes[start]
            ex, ey = vertexes[end]
            distance = abs(sx - ex) + abs(sy - ey)
            graph[start][end] = distance
            graph[end][start] = distance
            
    result = False
    start, end = 0, n + 1
    
    visited = [0] * (n + 2)
    visited[start] = 1
    
    queue = collections.deque()
    queue.append(start)
    
    while queue:
        vertex = queue.popleft()
        
        if vertex == end:
            result = True
            break
        
        for next in range(n + 2):
            if next != vertex and not visited[next] and graph[vertex][next] <= 1000:
                visited[next] = 1
                queue.append((next))
    
    print("happy" if result else "sad")