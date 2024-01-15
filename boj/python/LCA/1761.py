import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

MAX_DEPTH = 16

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, cost = map(int, input().split())
    
    graph[a].append((b, cost))
    graph[b].append((a, cost))
    
parent = [ [0] * MAX_DEPTH for _ in range(n + 1) ]
distance = [ [0] * MAX_DEPTH for _ in range(n + 1) ]
depth = [ 0 ] * (n + 1)

def dfs(node):
    for next, cost in graph[node]:
        if not depth[next]:
            depth[next] = depth[node] + 1
            parent[next][0] = node
            distance[next][0] = cost
            dfs(next)

depth[1] = 1
dfs(1)

for pow in range(1, MAX_DEPTH):
    for node in range(1, n + 1):
        prev = parent[node][pow - 1]
        if prev:
            parent[node][pow] = parent[ prev ][pow - 1]
            distance[node][pow] = distance[node][pow - 1] + distance[ prev ][pow - 1]
    
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    
    if depth[a] < depth[b]:
        a, b = b, a
    
    cost = 0
    for x in range(MAX_DEPTH - 1, -1, -1):
        if depth[a] - depth[b] >= 2 ** x:
            cost += distance[a][x]
            a = parent[a][x]
    
    if a != b:
        for pow in range(MAX_DEPTH - 1, -1, -1):
            if parent[a][pow] and parent[a][pow] != parent[b][pow]:
                cost += (distance[a][pow] + distance[b][pow])
                a = parent[a][pow]
                b = parent[b][pow]
        
        cost += (distance[a][0] + distance[b][0])
        a = parent[a][0]
    
    print(cost)