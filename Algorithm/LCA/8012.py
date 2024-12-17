from sys import stdin, setrecursionlimit
setrecursionlimit(150000)
input = stdin.readline

MAX_DEPTH = 17

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

depths = [ 0 ] * (n + 1)
parent = [ [ 0 ] *  MAX_DEPTH for _ in range(n + 1) ]

def dfs(node, depth):
    depths[node] = depth
    for next in graph[node]:
        if not depths[next]:
            parent[next][0] = node
            dfs(next, depth + 1)
            
def LCA(u, v):
    cost = 0
    if depths[u] < depths[v]:
        u, v = v, u
    
    for x in range(MAX_DEPTH - 1, -1, -1):
        if depths[u] - depths[v] >= 2 ** x:
            cost += 2 ** x
            u = parent[u][x]
    
    if u != v:
        for x in range(MAX_DEPTH - 1, -1, -1):
            if parent[u][x] and parent[u][x] != parent[v][x]:
                u = parent[u][x]
                v = parent[v][x]
                
                cost += 2 ** (x + 1)
        
        cost += 2
    
    return cost

dfs(1, 1)

for pow in range(1, MAX_DEPTH):
    for node in range(1, n + 1):
        parent[node][pow] = parent[ parent[node][pow-1] ][pow-1]

m = int(input())
start, cost = 1, 0
for _ in range(m):
    end = int(input())
    distance = LCA(start, end)
    
    start = end
    cost += distance
    
print(cost)