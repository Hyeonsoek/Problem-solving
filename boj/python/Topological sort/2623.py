import sys, collections
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n + 1)
array = [[] for _ in range(n + 1)]

for _ in range(m):
    k, *a = map(int, input().split())
    
    for x in range(k - 1):
        indegree[a[x+1]] += 1
        array[a[x]].append(a[x+1])
        
queue = collections.deque()
for x in range(1, n + 1):
    if not indegree[x]:
        queue.append(x)
        
result = []
for x in range(1, n + 1):
    if queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for next in array[vertex]:
            indegree[next] -= 1
            if not indegree[next]:
                queue.append(next)
    else:
        print("0")
        exit(0)

print(*result, sep='\n')