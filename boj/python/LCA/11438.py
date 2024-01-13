import sys
#setrecursionlimit 10**6 << memory limit exceeded
sys.setrecursionlimit(100000)

input = sys.stdin.readline

MAX_DEPTH = 17

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    
    tree[a].append(b)
    tree[b].append(a)

depths = [ 0 ] * (n + 1)
parents = [[0] * MAX_DEPTH for _ in range(n + 1)]

def dfs(vertex):
    for next in tree[vertex]:
        if not depths[next]:
            parents[next][0] = vertex
            depths[next] = depths[vertex] + 1
            dfs(next)

depths[1] = 1
dfs(1)

for depth in range(1, MAX_DEPTH):
    for node in range(1, n + 1):
        parents[node][depth] = parents[ parents[node][depth - 1] ][depth - 1]
    
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    
    if depths[a] < depths[b]:
        a, b = b, a
    
    for x in range(MAX_DEPTH - 1, -1, -1):
        if depths[a] - depths[b] >= 2 ** x:
            a = parents[a][x]
    
    if a != b:
        for depth in range(MAX_DEPTH - 1, -1, -1):
            if parents[a][depth] and parents[a][depth] != parents[b][depth]:
                a = parents[a][depth]
                b = parents[b][depth]
    
        a = parents[a][0]
    
    print(a)