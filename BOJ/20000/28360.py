n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bucket = [0] * (n + 1)
bucket[1] = 100

for x in range(1, n + 1):
    for nbr in graph[x]:
        bucket[nbr] += bucket[x] / len(graph[x])

result = 0
for x in range(1, n + 1):
    if not graph[x]:
        result = max(result, bucket[x])
    
print(result)