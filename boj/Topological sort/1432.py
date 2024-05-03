import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
indegree = [ 0 ] * n

for x in range(n):
    inputs = list(map(int, list(input().rstrip())))
    for y, value in enumerate(inputs):
        if value:
            graph[y].append(x)
            indegree[x] += 1

queue = PriorityQueue()
for x in range(n):
    if not indegree[x]:
        queue.put(-x)

count = n
result = [0] * n
for x in range(n):
    if not queue.empty():
        vertex = -queue.get()
        
        result[vertex] = count
        count -= 1
        
        for next in graph[vertex]:
            indegree[next] -= 1
            if not indegree[next]:
                queue.put(-next)
    else:
        print(-1)
        exit(0)

print(*result)