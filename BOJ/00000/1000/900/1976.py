import sys, collections
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [ list(map(int, input().split())) for _ in range(n) ]
order = list(map(int, input().split()))

for x in range(m-1):
    result = False
    start = order[x] - 1
    end = order[x+1] - 1
    
    visited = [0] * n
    visited[start] = 1
    
    queue = collections.deque()
    queue.append(start)
    
    while queue:
        vertex = queue.popleft()
        
        if vertex == end:
            result = True
            break
        
        for next in range(n):
            if next != vertex and not visited[next] and graph[vertex][next]:
                visited[next] = 1
                queue.append(next)
        
    if not result:
        print("NO")
        exit(0)
        
print("YES")