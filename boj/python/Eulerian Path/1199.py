import sys
input = sys.stdin.readline

n = int(input())
degree = [0] * n
counts = []
graph = [ dict() for _ in range(n) ]

for x in range(n):
    line = list(map(int, input().split()))
    counts.append(line)
    for y in range(n):
        if line[y]:
            graph[x][y] = 1
            degree[x] += line[y]
        
for x in range(n):
    if degree[x] % 2:
        print(-1)
        exit(0)

result = []
stack = [0]
while stack:
    vertex = stack[-1]
    if graph[vertex]:
        _next = next(iter(graph[vertex]))
        counts[vertex][_next] -= 1
        counts[_next][vertex] -= 1
        degree[vertex] -= 1
        degree[_next] -= 1
        
        if not counts[vertex][_next]:
            del graph[vertex][_next]
            del graph[_next][vertex]
        
        stack.append(_next)
    else:
        result.append(str(stack.pop() + 1))

for x in range(n):
    if degree[x]:
        print(-1)
        exit(0)
    
print(" ".join(result))