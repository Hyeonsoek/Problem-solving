import sys, collections
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]

for x in range(m):
    start, end = map(int, input().split())
    adj[start].append(end)
    indegree[end] += 1

result = [0] * (n+1)
queue = collections.deque()
for x in range(1, n + 1):
    if not indegree[x]:
        queue.append(x)
        
for x in range(1, n + 1):
    if queue:
        vertex = queue.popleft()
        result[x] = vertex
        
        for next in adj[vertex]:
            indegree[next] -= 1
            if not indegree[next]:
                queue.append(next)

print(*result[1:])