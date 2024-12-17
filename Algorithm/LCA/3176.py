from sys import stdin, setrecursionlimit
setrecursionlimit(100000)
input = stdin.readline

MAX_DEPTH = 17

def min_max(target : tuple, *nexts : tuple) -> tuple:
    result_min, result_max = target

    for mmin, mmax in nexts:
        result_min = min(result_min, mmin)
        result_max = max(result_max, mmax)

    return (result_min, result_max)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, cost = map(int, input().split())
    
    graph[a].append((b, cost))
    graph[b].append((a, cost))

parent = [ [ 0 ] * MAX_DEPTH for _ in range(n + 1) ]
distance = [ [ (0, 0) for _ in range(MAX_DEPTH) ] for _ in range(n + 1) ]
depth = [ 0 ] * (n + 1)

def dfs(node):
    for next, cost in graph[node]:
        if not depth[next]:
            depth[next] = depth[node] + 1
            parent[next][0] = node
            distance[next][0] = (cost, cost)
            dfs(next)

dfs(1)

for pow in range(1, MAX_DEPTH):
    for node in range(1, n + 1):
        prev = parent[node][pow - 1]
        parent[node][pow] = parent[ prev ][pow - 1]
        distance[node][pow] = min_max(distance[node][pow - 1], distance[ prev ][pow - 1])

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    
    if depth[a] < depth[b]:
        a, b = b, a
    
    result = (1000000, 0)
    for x in range(MAX_DEPTH - 1, -1, -1):
        if depth[a] - depth[b] >= 2 ** x:
            result = min_max(result, distance[a][x])
            a = parent[a][x]
    
    if a != b:
        for pow in range(MAX_DEPTH - 1, -1, -1):
            if parent[a][pow] and parent[a][pow] != parent[b][pow]:
                result = min_max(distance[a][pow], distance[b][pow], result)
                
                a = parent[a][pow]
                b = parent[b][pow]
        
        result = min_max(distance[a][pow], distance[b][pow], result)
        a = parent[a][pow]
    
    print(*result)