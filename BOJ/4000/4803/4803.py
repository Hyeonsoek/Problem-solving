import sys
from collections import deque
input = sys.stdin.readline

def solve(index, n, m):
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    count = 0
    visited = [False] * (n + 1)
    for x in range(1, n + 1):
        if visited[x] == False:
            vertcount = 0
            edgecount = 0
            visited[x] = True
            queue = deque([x])
            while queue:
                vertex = queue.popleft()
                vertcount += 1
                edgecount += len(graph[vertex])
                
                for next in graph[vertex]:
                    if visited[next] == False:
                        visited[next] = True
                        queue.append(next)
            
            count += int((edgecount >> 1) == vertcount - 1)
    
    result = f"Case {index}: "
    
    if count > 1:
        result += f'A forest of {count} trees.'
    elif count == 1:
        result += 'There is one tree.'
    else:
        result += 'No trees.'
    
    print(result)

index = 1
while (i := input().strip()) != '0 0':
    solve(index, *map(int, i.split()))
    index += 1